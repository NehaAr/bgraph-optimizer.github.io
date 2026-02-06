from .common_imports import *
from multiprocessing.dummy import Pool
#Adds shell to the graph


def shell(node_list: List[str],interaction_type: str,interactors: int,required_score: int) ->List[str]:
    """
    This module adds the shells to the network. There are two modes to run the network. One is Direct and another one is Indirect.

    Direct: It adds the proteins which are directly linked to the proteins 
    Indirect: It adds the proteins which are linked to each other transitively A-B,B-C then it records the indirect interaction as A-B-C

    Arguments:
    node_list= It is the list of proteins whose interactions need to be added.
    interaction_type: It specifies the type of interaction(Direct or Indirect).
    interactor:It specifies the number of proteins tobe added.
    required_score: The confidence score in hundreds. There are four thresholds for score as follows:
   
    low confidence - 0.15 (or better), becomes 150 for API
    medium confidence - 0.4, becomes 400 for API
    high confidence - 0.7, becomes 700 for API
    highest confidence - 0.9, becomes 900 for API

    Return:
    edges_to_add - A tuple of edges to be added to the network

    """
  
    global empty_df 

    def fetch_url(url):
       response=requests.get(url)
       return response

    def has_interaction(a, b, df):
            
            return (
                 df[(df['Protein_name'] == a) & (df['Drug_name'] == b)].any().any()
                             or
                 df[(df['Protein_name'] == b) & (df['Drug_name'] == a)].any().any()
                                )
    
    edges_to_add=[]
    empty_df=pd.DataFrame()
    for i in set(node_list):
        # Make sure the API request URL is correct for fetching PPI images
           def fetch_data():
              url1 = f"https://string-db.org/api/tsv/interaction_partners?identifiers={i}&species=9606&required_score={required_score}&network_type=functional&limit=1000"
              url2=f"https://string-db.org/api/tsv/interaction_partners?identifiers={i}&species=9606&required_score={required_score}&network_type=physical&limit=200000"
              with ThreadPoolExecutor(max_workers=2) as executor:
               response1,response2=executor.map(fetch_url,[url1, url2])
               return response1,response2

           response1,response2 = fetch_data()
           if response1.status_code == 200 and response2.status_code==200:
            # Save the image temporarily
              file = pd.read_csv(io.StringIO(response1.text), sep="\t")
              file1 = pd.read_csv(io.StringIO(response2.text), sep="\t")
              file=file[['stringId_A', 'stringId_B', 'preferredName_A', 'preferredName_B', 'score',
               'escore', 'dscore', 'tscore']]
              file1=file1[['stringId_A', 'stringId_B', 'preferredName_A', 'preferredName_B', 'score',
               'escore', 'dscore', 'tscore']]
              file.rename(columns={'stringId_A':'Protein','stringId_B':'Drug','preferredName_A':'Protein_name','preferredName_B':'Drug_name'\
              ,'score':'score1'},inplace=True)
              file=file.sort_values(by=['score1','escore','tscore'],ascending=False)
              file1.rename(columns={'stringId_A':'Protein','stringId_B':'Drug','preferredName_A':'Protein_name','preferredName_B':'Drug_name'\
              ,'score':'score1'},inplace=True)
              file1=file1.sort_values(by=['score1','escore','tscore'],ascending=False)
              file=pd.concat([file,file1])
             
              if interaction_type=="direct":
                 if interactors<=len(file): 
                   file=file[:interactors]        
                 edges_to_add.extend(list(zip(file['Protein_name'], file['Drug_name'])))
                 empty_df=pd.concat([empty_df, file], axis=0)
              elif interaction_type=="indirect":                    
                 nodes = file['Drug_name'].unique()
                 nodes=[n for n in nodes if n!=i]
                 nodes.append(i)                
                 identifiers = "%0d".join(nodes)
                 url_new = (
                 f"https://string-db.org/api/tsv/network"
                 f"?identifiers={identifiers}&required_score={required_score}&species=9606&limit=1000"
                      )
                 response_new= requests.get(url_new)
                 file_new = pd.read_csv(io.StringIO(response_new.text), sep="\t")
                 file_new=file_new[['stringId_A', 'stringId_B', 'preferredName_A', 'preferredName_B', 'score',
                       'escore', 'dscore', 'tscore']]                       
                 file_new.rename(columns={'stringId_A':'Protein',\
                 'stringId_B':'Drug','preferredName_A':'Protein_name',\
                 'preferredName_B':'Drug_name','score':'score1'},inplace=True)
                 if interactors<=len(file_new):
                     file_new=file_new[:interactors]
                 # Build a fast lookup set
                 interaction_set = set()
                 for a, b in zip(file_new["Protein_name"], file_new["Drug_name"]):
                       interaction_set.add((a, b))
                       interaction_set.add((b, a))
                 def has_interaction_fast(a, b, interaction_set):
                        return (a, b) in interaction_set

                 items=combinations(nodes,3)
                 tasks=[(i,j,m,interaction_set) for i,j,m in items]
                 def process_iterations(i,j,m,interaction_set):
                     ij = has_interaction_fast(i, j, interaction_set)
                     jm = has_interaction_fast(j, m, interaction_set)
                     im = has_interaction_fast(m, i, interaction_set)
                     if ij and jm and not im:
                       print(f"Indirect interaction detected: {i} -- {j} -- {m}")
                       edges_to_add.append((i,j))
                       edges_to_add.append((j,m))
                       edges_to_add.append((i,m))
                                           
                 with Pool() as pool:
                    asyn_result=pool.starmap_async(process_iterations, tasks)
                    result=asyn_result.get()               
    return edges_to_add

def string_io(node_list: List[str],interaction_type: str,interactors: int,required_score: int,aggregator=shell)-> None:
     
   edges_to_add=aggregator(node_list,interaction_type,interactors,required_score)
   G=nx.Graph()
   G.add_edges_from(edges_to_add)
   pos=nx.spring_layout(G,k=0.7)
   colors = [plt.cm.viridis(i / len(G.nodes())) for i in range(len(G.nodes()))]
   plt.figure(figsize=(15,15))
   nx.draw(G,node_size=300 ,with_labels=True,pos=pos,edge_color="gray",width=0.5,node_color=colors,font_size=3)
   plt.tight_layout()
   plt.show()

def expand_shells(G,node_list, max_shells=5, hub_threshold=0.3):
      current_nodes = set(node_list)
      prev_metrics = None
      for shells in range(max_shells+1):
        # Add 1 shell of neighbors
        new_nodes = set()
        for node in current_nodes:
            new_nodes.update(G.neighbors(node))
        new_nodes = new_nodes - current_nodes  # only new additions
        current_nodes.update(new_nodes)

        # Build subgraph
        subG = G.subgraph(current_nodes).copy()

        # Compute metrics
        avg_path = nx.average_shortest_path_length(subG) if nx.is_connected(subG) else None
        density = nx.density(subG)
        clustering = nx.average_clustering(subG)
        degrees = [d for n, d in subG.degree()]
        top_deg_frac = max(degrees) / sum(degrees)  # hub domination fraction
        new_nodes_ratio = len(new_nodes) / G.number_of_nodes()
        print(f"Shell {shells}: Nodes={len(subG)}, Density={density:.3f}, Clustering={clustering:.3f}, Hub fraction={top_deg_frac:.3f},\
             Avg path={avg_path}")
        prev_metrics = (avg_path, density, clustering, top_deg_frac)
        # Stopping criteria
        if prev_metrics:
            # Example: stop if hub domination > threshold or density jumps
            if top_deg_frac >= hub_threshold or new_nodes_ratio < 0.05:
                print(f"Stopping at shell {shells} due to hub domination")
                break
            else:
                interaction_type=input("Enter the type of interaction")
                print(new_nodes)
                edges_to_add=shell(new_nodes,interaction_type,1000,800)
                print(edges_to_add)
                G.add_edges_from(edges_to_add)
                expand_shells(G,new_nodes, max_shells=5, hub_threshold=0.3)

      return subG

# Benchmark Results

## 1. Overview
This document summarizes the performance benchmarks of the project using Python interpreters and relevant libraries.

## 2. Environment

| Parameter | Value |
|-----------|-------|
| Operating System | macOS 14 / Windows 11 |
| CPU | Apple M4(sequoia 15.7.2)/Intel Core i7-9750H / |
| RAM | 16 GB |
| Python version | 3.13 (macOS), 3.12 (Windows) |
| PyPy version | 7.3.12 (if applicable) |
| Benchmark tool | Pystone 1.1 |

## 3. Pystone Benchmark

| Interpreter | OS | Passes | Time (s) | Pystones/sec |
|------------|----|-------|-----------|---------------|
| CPython 3.13 | macOS | 50,000 | 00.0704142 | 710084 |
| CPython 3.12 | Windows | 50,000 | 0.07504533 | 666264 |
| PyPy3 7.3 | Windows | 50,000 | 0.0241771 | 2068070 |

> Notes: Slight differences in pystones/sec are due to Python version, OS, CPU architecture, and background processes.

# 4. Python Performance Benchmarks(pyperformance)

**Python Performance Version:** 1.13.0  
**Operating System:** Windows 11 (Build 22631)  
**Logical CPUs:** 12  
**Benchmark Start:** 2025-12-08 14:26:53  
**Benchmark End:** 2025-12-08 16:21:44  

---

## Summary

A series of Python performance benchmarks were executed on this machine.  
Each test reports **mean execution time** and **standard deviation**.

One benchmark failed:

- `dulwich_log` – *Install requirements error*

---

## Benchmark Results

### xml_etree
| Test | Mean | Std Dev |
|------|------|---------|
| xml_etree_process | 47.9 ms | 2.9 ms |
| xml_etree_parse | 119 ms | 6 ms |
| xml_etree_iterparse | 84.0 ms | 4.3 ms |
| xml_etree_generate | 71.8 ms | 3.5 ms |

### 2to3
| Test | Mean | Std Dev |
|------|------|---------|
| 2to3 | 579 ms | 29 ms |

### Async Benchmarks
| Test | Mean | Std Dev |
|------|------|---------|
| async_generators | 469 ms | 59 ms |
| async_tree_none | 424 ms | 32 ms |
| async_tree_cpu_io_mixed | 642 ms | 31 ms |
| async_tree_cpu_io_mixed_tg | 703 ms | 93 ms |
| async_tree_eager | 95.5 ms | 5.5 ms |
| async_tree_eager_cpu_io_mixed | 447 ms | 51 ms |
| async_tree_eager_cpu_io_mixed_tg | 362 ms | 26 ms |
| async_tree_eager_io | 958 ms | 59 ms |
| async_tree_eager_io_tg | 955 ms | 37 ms |
| async_tree_eager_memoization | 220 ms | 15 ms |
| async_tree_eager_memoization_tg | 181 ms | 8 ms |
| async_tree_eager_tg | 61.7 ms | 4.3 ms |
| async_tree_io | 939 ms | 42 ms |
| async_tree_io_tg | 983 ms | 72 ms |
| async_tree_memoization | 490 ms | 23 ms |
| async_tree_memoization_tg | 463 ms | 25 ms |
| async_tree_none_tg | 381 ms | 22 ms |

### Networking / IO Benchmarks
| Test | Mean | Std Dev |
|------|------|---------|
| asyncio_tcp | 1.01 sec | 0.07 sec |
| asyncio_tcp_ssl | 3.88 sec | 0.49 sec |
| asyncio_websockets | 717 ms | 71 ms |

### Tokenizer
| Test | Mean | Std Dev |
|------|------|---------|
| bpe_tokeniser | 7.14 sec | 0.77 sec |

### Template Engines
| Test | Mean | Std Dev |
|------|------|---------|
| chameleon | 19.2 ms | 2.2 ms |
| django_template | 33.7 ms | 2.2 ms |
| mako | 9.66 ms | 0.45 ms |

### JSON Benchmarks
| Test | Mean | Std Dev |
|------|------|---------|
| json_dumps | 9.67 ms | 3.75 ms |
| json_loads | 20.2 µs | 6.7 µs |

### Logging
| Test | Mean | Std Dev |
|------|------|---------|
| logging_format | 9.95 µs | 1.95 µs |
| logging_silent | 82.3 ns | 5.8 ns |
| logging_simple | 8.85 µs | 0.28 µs |

### Multiprocessing / Threading
| Test | Mean | Std Dev |
|------|------|---------|
| bench_mp_pool | 544 ms | 52 ms |
| bench_thread_pool | 2.78 ms | 0.66 ms |

### Crypto
| Test | Mean | Std Dev |
|------|------|---------|
| crypto_pyaes | 70.4 ms | 13.3 ms |

### Dask
| Test | Mean | Std Dev |
|------|------|---------|
| dask | 1.41 sec | 0.31 sec |

### Deepcopy
| Test | Mean | Std Dev |
|------|------|---------|
| deepcopy | 326 µs | 34 µs |
| deepcopy_reduce | 2.94 µs | 0.22 µs |
| deepcopy_memo | 31.1 µs | 2.3 µs |


## Failed Benchmarks

| Benchmark | Reason |
|----------|--------|
| dulwich_log | Install requirements error |

---

## Notes

- All times represent the arithmetic mean over multiple repetitions.
- Standard deviation reflects stability of performance.
- Large variations may indicate CPU throttling, background processes, or system load.

---


## 5. Additional Benchmarks
- Optional: Include `timeit`, or other custom benchmarks.
- Compare scripts and interpreter performance.

## 6. Recommendations
- Use PyPy for CPU-heavy pure Python code.  
- Use CPython for maximum compatibility with C extensions.  

## 7. References
- [Python Pystone Documentation](https://docs.python.org/3/library/test.html#module-test.pystone)  
- [PyPerformance](https://github.com/python/pyperformance)

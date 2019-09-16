#[macro_use]
extern crate cpython;

use cpython::{Python, PyResult};

fn fibonacci(_py: Python, n: u32) -> PyResult<u32>{
    if n < 2 {
        return Ok(1)
    }
    let mut prev1 = 1;
    let mut prev2 = 1;
    for _ in 1..n {
        let new = prev1 + prev2;
        prev2 = prev1;
        prev1 = new;
    }
    Ok(prev1) 
}

py_module_initializer!(hello, inithello, PyInit_hello, |py, m | {
    m.add(py, "__doc__", "This module is implemented in Rust")?;
    m.add(py, "fib", py_fn!(py, fibonacci(n: u32)))?;
    Ok(())
});

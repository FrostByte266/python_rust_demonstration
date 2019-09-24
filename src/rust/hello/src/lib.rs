#![deny(rust_2018_idioms)]
use ndarray::{ArrayViewD};
use numpy::{PyArrayDyn};
use pyo3::prelude::{pymodule, PyModule, PyResult, Python};

#[pymodule]
fn rustic(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    fn get_angle(a: ArrayViewD<'_, f64>, b: ArrayViewD<'_, f64>, c: ArrayViewD<'_, f64>) -> PyResult<f64> {
        let c1b1 = c[1] - b[1];
        let c0b0 = c[0] - b[0];
        let a1b1 = a[1] - b[1];
        let a0b0 = a[0] - b[0];

        Ok(((c1b1.atan2(c0b0) - a1b1.atan2(a0b0)).to_degrees()).abs())
    }

    #[pyfn(m, "get_angle")]
    fn get_angle_py(
        _py: Python<'_>,
        a: &PyArrayDyn<f64>,
        b: &PyArrayDyn<f64>,
        c: &PyArrayDyn<f64>,
    ) -> PyResult<f64> {
        let a = a.as_array();
        let b = b.as_array();
        let c = c.as_array();
        get_angle(a, b, c)
    }


    Ok(())
}
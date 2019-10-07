use ndarray::{ArrayViewD, ArrayViewMutD};
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
    fn find_distance(a: ArrayViewD<'_, f64>, b: ArrayViewD<'_, f64>) -> PyResult<f64> {
        let y_diff = b[1] - a[1];
        let x_diff = b[0] - a[0];

        let y_diff_squared = y_diff.powi(2);
        let x_diff_squared = x_diff.powi(2);

        let sum_square_diff = y_diff_squared + x_diff_squared;

        Ok(sum_square_diff.sqrt())
    }

    fn gen_circle_points(r: f64, mut x: ArrayViewMutD<'_, f64>, mut y: ArrayViewMutD<'_, f64>) {
        for i in 0..x.len() {
            x[i] = r * f64::cos(x[i]);
            y[i] = r * f64::sin(y[i]);
        }
    }

    #[pyfn(m, "get_angle")]
    fn get_angle_py(
        _py: Python<'_>,
        a: &PyArrayDyn<f64>,
        b: &PyArrayDyn<f64>,
        c: &PyArrayDyn<f64>
    ) -> PyResult<f64> {
        let a = a.as_array();
        let b = b.as_array();
        let c = c.as_array();
        get_angle(a, b, c)
    }

    #[pyfn(m, "find_distance")]
    fn find_distance_py(
        _py: Python<'_>,
        a: &PyArrayDyn<f64>,
        b: &PyArrayDyn<f64>
    ) -> PyResult<f64> {
        let a = a.as_array();
        let b = b.as_array();
        find_distance(a, b)
    }

    #[pyfn(m, "gen_circle_points")]
    fn gen_circle_points_py(
        _py: Python<'_>,
        r: f64,
        x: &PyArrayDyn<f64>,
        y: &PyArrayDyn<f64>
    ) -> PyResult<()> {
        let x = x.as_array_mut();
        let y = y.as_array_mut();
        gen_circle_points(r, x, y);
        Ok(())
    }

    Ok(())
}
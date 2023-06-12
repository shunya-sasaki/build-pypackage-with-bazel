/**
 * @file cpp.cpp
 * @author Shunya Sasaki (shunya.sasaki1120@gmail.com)
 * @brief 
 * @details
 * @date 2023-06-03
 */
#include <iostream>
#include <pybind11/pybind11.h>

/**
 * @brief A function which prints Hello, World!
 *
 */
void hello()
{
    std::cout << "Hello, World!" << std::endl;
    return;
}

/**
 * @brief A function which adds two numbers
 *
 * @tparam T Number type
 * @param a A number
 * @param b A number
 * @return T Sum of a and b
 */
template <typename T>
T add(T a, T b)
{
    return a + b;
}

/**
 * @brief Construct a new pybind11 module object
 * 
 */
PYBIND11_MODULE(lib, m)
{
    m.doc() = "pybind11 example plugin"; // optional module docstring
    m.def("hello", &hello, "A function which prints Hello, World!");
    m.def("add", &add<int>, "A function which adds two numbers");
    m.def("add", &add<float>, "A function which adds two numbers");
    m.def("add", &add<double>, "A function which adds two numbers");
}

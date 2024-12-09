#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include "verilated.h"
#include "Vtop.h"  // Verilator 生成的顶层模块

class SimulatorInterface {
private:
    Vtop* top;
    bool running;
    std::vector<uint8_t> display_buffer;
    
public:
    SimulatorInterface() : top(new Vtop), running(false) {
        display_buffer.resize(400 * 300);
    }
    
    ~SimulatorInterface() {
        delete top;
    }
    
    void start() {
        running = true;
    }
    
    void stop() {
        running = false;
    }
    
    void set_led(int id, bool status) {
        // 设置 LED 输入信号
        switch(id) {
            case 0: top->led_0 = status; break;
            case 1: top->led_1 = status; break;
            // ... 更多 LED
        }
        // 执行一个时钟周期
        top->eval();
    }
    
    void set_switch(int id, bool status) {
        // 设置开关输入信号
        switch(id) {
            case 0: top->switch_0 = status; break;
            case 1: top->switch_1 = status; break;
            // ... 更多开关
        }
        top->eval();
    }
    
    std::vector<uint8_t> get_display_data() {
        // 从模拟器获取显示数据
        // 这里需要根据您的 Verilog 代码来实现
        return display_buffer;
    }
    
    std::vector<bool> get_seven_segment_data() {
        // 获取七段数码管状态
        std::vector<bool> segments;
        // 从模拟器获取数据
        return segments;
    }
};

PYBIND11_MODULE(simulator_interface, m) {
    py::class_<SimulatorInterface>(m, "SimulatorInterface")
        .def(py::init<>())
        .def("start", &SimulatorInterface::start)
        .def("stop", &SimulatorInterface::stop)
        .def("set_led", &SimulatorInterface::set_led)
        .def("set_switch", &SimulatorInterface::set_switch)
        .def("get_display_data", &SimulatorInterface::get_display_data)
        .def("get_seven_segment_data", &SimulatorInterface::get_seven_segment_data);
} 
#include <memory>

#include <rclcpp/rclcpp.hpp>
#include<std_msgs/msg/string.hpp>
//#include<std_msgs/msg/int32.hpp>

using std::placeholders::_1;

class Sub : public rclcpp::Node{
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr sub_;
    //rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr sub_;

    public:
        Sub() : Node("sub_node"){
            sub_ = this->create_subscription<std_msgs::msg::String>("topic", 10, std::bind(&Sub::sub_callback, this, _1));
            //sub_ = this->create_subscription<std_msgs::msg::Int32>("joush", 10, std::bind(&Sub::sub_callback, this, _1));
        }

    private:
        void sub_callback(const std_msgs::msg::String &msg) const{
            RCLCPP_INFO(this->get_logger(), "Me está llegando: '%s'", msg.data.c_str());
        }
};

int main(int argc, char *argv[]){

    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<Sub>());
    rclcpp::shutdown();
    return 0;

}
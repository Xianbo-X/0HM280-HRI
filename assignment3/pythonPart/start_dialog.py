#Simple dialog in Python
# -*- encoding: UTF-8 -*-

from naoqi import ALProxy


def start_dialog_on_multitopics(robot_ip, robot_port, topf_path, threshold=0.4):
    dialog_p = ALProxy('ALDialog', robot_ip, robot_port)
    dialog_p.setLanguage("English")
    dialog_p.setASRConfidenceThreshold(threshold)

    num_topic = len(topf_path)
    topic = []
    # Load topic - absolute path is required
    for i in range(num_topic):
        topf_path[i] = topf_path[i].decode('utf-8')
        topic.append(dialog_p.loadTopic(topf_path[i].encode('utf-8')))

    # Start dialog
    dialog_p.subscribe('myModule')

    # Activate dialog
    for i in range(num_topic):
        dialog_p.activateTopic(topic[i])
    
    # dialog_p.setFocus()

    raw_input(u"Press 'Enter' to exit.")

    for i in range(num_topic):
        # Deactivate topic
        dialog_p.deactivateTopic(topic[i])

        # Unload topic
        dialog_p.unloadTopic(topic[i])

    # Stop dialog
    dialog_p.unsubscribe('myModule')

if __name__ == '__main__':
    dialog_topic = []
    # dialog_topic = "/home/nao/group_08/mydialog_enu.top"  # Absolute path of the dialog topic file (on the robot).
    dialog_topic.append("/home/nao/group_08/Topics/checkin_enu.top")  # Absolute path of the dialog topic file (on the robot).
    dialog_topic.append("/home/nao/group_08/Topics/food_enu.top")
    dialog_topic.append("/home/nao/group_08/Topics/general_enu.top")
    dialog_topic.append("/home/nao/group_08/Topics/test_enu.top")
    # robot_ip="127.0.0.1" # replace this with the actual ip address of the robot
    # robot_ip="192.168.0.119" #
    # robot_ip="192.168.0.115" #
    robot_ip="192.168.0.112" # 
    # robot_ip="192.168.0.119"
    port=9559 # Robot port number

    start_dialog_on_multitopics(robot_ip, port, dialog_topic)

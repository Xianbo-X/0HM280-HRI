import nao_nocv_2_1 as nao

def start_dialog_on_multitopics(event,topf_path, threshold=0.4):
    # dialog_p = ALProxy('ALDialog', robot_ip, robot_port)
    print("thread start")
    dialog_p = nao.dialogProxy
    dialog_p.setLanguage("English")
    dialog_p.setASRConfidenceThreshold(threshold)

    num_topic = len(topf_path)
    topic = []
    # Load topic - absolute path is required
    for i in range(num_topic):
        topf_path[i] = topf_path[i].decode('utf-8')
        topic.append(dialog_p.loadTopic(topf_path[i].encode('utf-8'))) # load all topics

    try:
        # Start dialog
        dialog_p.subscribe('myModule')

        # Activate dialog
        for i in range(num_topic):
            dialog_p.activateTopic(topic[i]) # activate all topics
        
        # dialog_p.setFocus()
        event.wait()
        print("Thread exit")
        # raw_input(u"Press 'Enter' to exit.")
    except Exception,e:
        print "Exception happened:",e
    finally:
        for i in range(num_topic):
            # Deactivate topic
            dialog_p.deactivateTopic(topic[i])

            # Unload topic
            dialog_p.unloadTopic(topic[i])

        # Stop dialog
        dialog_p.unsubscribe('myModule')
    Response="YES" #TODO: Change to get a response from dialog
    return Response
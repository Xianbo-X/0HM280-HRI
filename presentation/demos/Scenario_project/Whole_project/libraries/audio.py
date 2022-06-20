import nao_nocv_2_1 as nao
import time
DEBUG=False

def speech_recog(wordList,maxcount=50,subscriber_name="MyModule"):
    if DEBUG:
        result=raw_input("Enter the word from: "+str(wordList))
        print "Get results", result
        return result
    the_language="English"
    result=None
    nao.InitSpeech(wordList,the_language)
    count=0
    nao.asr.subscribe(subscriber_name)
    while count<maxcount:
        #nao.memoryProxy.insertData("WordRecognized",[])

        result=nao.DetectSpeech()
        #print result
        if len(result)>0:
            print result
            nao.asr.unsubscribe(subscriber_name)
            return result[0]
            # nao.Say("You said: "+result[0]+".")
            # time.sleep(0.2)
            # nao.asr.subscribe(subscriber_name)
        time.sleep(0.2)
        count=count+1
    nao.asr.unsubscribe(subscriber_name)
    return "NoResult"
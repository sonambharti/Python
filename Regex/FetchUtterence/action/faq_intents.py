

class ActionGreet(Action):
    def name(self):
        return "action_greet"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message.get("intent").get("name")
        greet_count = tracker.get_slot("greet_count")
        user_message = tracker.latest_message.get("text")
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        SRP = SRP_value(customer_language,region)
        gender = tracker.get_slot("gender_slot")
        if intent == "greet":
            requested_slot = tracker.get_slot(REQUESTED_SLOT)
            if greet_count > 2:
                dispatcher.utter_template(
                "utter_disconnect_call_"+emi_flow+"_static"
                +SRP
                + bot_gender,
                tracker,)
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    user_message=user_message,
                    flag=TIMEOUT_FLAG,
                    disposition_details="MULTIPLE HELLO",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
            return_values = []
            if greet_count > 0:
                print("inside greet_count == 0")
                main_flow = tracker.active_form.get("name")
                print("main_flow", main_flow)
                if main_flow != "user_confirmation_form":
                    return_values.append(SlotSet("main_flow", main_flow))
                current_slot = tracker.get_slot(REQUESTED_SLOT)
                template = "utter_reply_greaterthan_5sec_"+emi_flow+"_static" + SRP+ bot_gender
                dispatcher.utter_template(template,tracker)
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    disposition_details="General - Greet",
                    emi_flow=emi_flow,
                )
               
            trail_count = tracker.get_slot("trail_count")

            else:
                template = "utter_reply_greaterthan_5sec_"+emi_flow+"_static" + SRP+ bot_gender
                dispatcher.utter_template(template,tracker)
                print("tracker.active_form.get() is not None -2")
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    disposition_details="General - Greet"
                )
                # dispatcher.utter_template("utter_ask_capability_common", tracker)
            print("tracker.active_form.get() is not None -3")
            return get_return_values(tracker) + [
                SlotSet("greet_count", greet_count + 1)
            ]
        else:
            print("emi flow",emi_flow)
            print("emi flow",SRP)
            print("emi flow",bot_gender)
            dispatcher.utter_template("utter_gibberish_b_"+emi_flow+"_static"+SRP+bot_gender, tracker)
            send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    disposition_details="Not - Understood"
                )
        return get_return_values(tracker)


class ActionWait(Action):
    def name(self):
        return "action_wait"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        wait_count = tracker.get_slot("wait_count")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        SRP = SRP_value(customer_language,region)
        print("jsdjfi")
        if wait_count < 2:
            dispatcher.utter_template(
                "utter_wait_"+emi_flow+"_static" + SRP + bot_gender, tracker
            )
            send_and_store_disposition_details(
                tracker=tracker,
                dispatcher=dispatcher,
                disposition_details="General - Wait",
                flag=WAIT_FLAG,
            )
            return [FollowupAction("action_listen"),
                    SlotSet("wait_count", wait_count + 1),
                    SlotSet]
            # return [
            #     SlotSet(REQUESTED_SLOT, None),
            #     SlotSet("trail_count", get_trail_count(tracker)),
            #     FollowupAction(tracker.active_form.get("name")),
            #     SlotSet("wait_count", wait_count + 1),
            # ]
        else:
            dispatcher.utter_template(
                "utter_request_for_customer_denied_"+emi_flow+"_static" + SRP + bot_gender, tracker
            )
            user_message = tracker.latest_message.get("text")
            # helper.send_conversation_flag(TIMEOUT_FLAG, dispatcher)
            send_and_store_disposition_details(
                tracker=tracker,
                dispatcher=dispatcher,
                flag= TIMEOUT_FLAG,
                disposition_details="General - Wait",
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
class ActionChangeLanguage(Action):
    def name(self):
        return "action_change_language"
    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message.get("temp_intent").get("name")
        change_language_count = tracker.get_slot("change_language_count")
        emi_flow = tracker.get_slot("emi_flow")
        language = tracker.get_slot("language")
        print("language",language)
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        print("customer_language",customer_language)
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        change_specific_language_count = tracker.get_slot("change_specific_language_count")
        text = tracker.latest_message.get("text")
        supported_languages = tracker.get_slot("supported_languages")
        supported_languages_1 = supported_languages.lower()
        supported_languages = supported_languages_1.split(",")
        nlu_data_list = tracker.get_slot("nlu_data_list_slot")
        requested_slot = tracker.get_slot(REQUESTED_SLOT)
        signal = tracker.latest_message.get("signal").get("name")
        print("163landayf",customer_language)
        print("The supported languages are", supported_languages)
        print("supported_languages->",supported_languages)
        print("change_language_count->",type(change_language_count),change_language_count)
        text = text.lower()
        print("text:::::::::::::::", text)
        all_languages = { #English,Hindi,Telugu,Kannada,Malayalam,Tamil,Bengali,Marathi,Punjabi,Gujarati ---> whatsapp
            "english":  ["english","eng","इंग्लिश","अंग्रेज़ी","अंग्रेजी","ఇంగ్లీష్","ఆంగ్ల","ಇಂಗ್ಲಿಷ್","ಇಂಗ್ಲೀಷ್","ಇಂಗ್ಲಿಶ್","ഇംഗ്ലീഷ്","ഇംഗ്ളീഷ്","இங்கிலீஷ்","இங்கிலிஷ்","ஆங்கிலம்",
                        "ইংলিশ","ইংরেজি","अंग्रेज़ी","अंग्रेझी","अंगरेझी","ਇੰਗਲਿਸ਼","ਅੰਗਰੇਜ਼ੀ","ઈંગ્લીશ","અંગ્રેજી","ઇંગ્લિશ","ഇംഗ്ലീഷു","ഇംഗ്ലിഷ്"],
            "hindi":    ["hindi","हिंदी","हिन्दी","हिंदि","హిందీ","హింది","హిన్దీ","హిన్ది","ಹಿಂದಿ","ಹಿಂದೀ","ഹിന്ദി","ഹിൻഡി","ஹிந்தி","இந்தி",
                        "হিন্দি","হিন্দী","हिन्दी","ਹਿੰਦੀ","ਹਿਦੀ","હિન્દી","હિંદી"],
            "telugu":   ["telugu","तेलुगु","तेलगू","తెలుగు","ತೆಲುಗು","ತೆಲುಗಿ","తెలుగులో","ತೆಲಗು","തെലുങ്ക്","തെലുങ്കു","തെലുഗു","തെലഗു","தெலுங்கு","தெலுகு",
                        "তেলেগু","তেলেগূ","तेलुगू","तेलगू","तेलगु","तेल्गु","तेल्गू","ਤੇਲਗੂ","ਤੇਲਗੁ","ਤੇਲੁਗੁ","ਤੇਲੁਗੂ","તેલુગુ","તેલૂગૂ","તેલુગૂ","તેલૂગુ"],
            "kannada":  ["kannada","कन्नड़","कन्नड़ा","कन्नड","కన్నడ","కన్నడా","కంనడ","ಕನ್ನಡ","ಕನ್ನಡ್","കന്നഡ","കന്നഡ്","கன்னட","கன்னடம்","கன்னடா",
           
        reverse_mapped_languages = {
            "en": "english",
            "hi": "hindi",
            "tam": "tamil",
            "tel": "telugu",
            "ka": "kannada",
            "ml": "malayalam",
            "ma": "marathi",
            "pa": "paunjabi",
            "bn": "bangla",
            "gu": "gujarati"
        }
        supported_dict = {}
        unsupported_dict = {}
        existed = 0
        unexisted = 0
        lan = []
        unlan = []
        # def lang_in_text(language,text):
        #     language = all_languages[language]
        #     words = text.split()
        #     result = False
        #     for i in language:
        #         matches = difflib.get_close_matches(i, words, n=1, cutoff=0.9)
        #         if matches:
        #             print("matched lang word",matches)
        #             result = True 
        #             break
        #     return result
        sup_lang_without_current_lang = supported_languages.copy()
        if intent == "ask":
            try:
                sup_lang_without_current_lang.remove(reverse_mapped_languages.get(customer_language,customer_language))
            except:
                pass
        print("supported_languagesssss",supported_languages)
        for key,value in all_languages.items():
            if key in sup_lang_without_current_lang:
                supported_dict[key] = value
        for key,value in supported_dict.items():
            for k in range(0,len(value)):
                if value[k] in text:
                    existed+=1
                    lan.append(key)
                    break
            # if lang_in_text(key,text):
            #     existed+=1
            #     lan.append(key)
            #     break
        print("faq258 lan",lan)
        if len(lan) > 1:
            try:
                lan.remove(reverse_mapped_languages.get(customer_language,customer_language))
            except:
                pass
        if lan != []:
            lan = lan[0]
        for key,value in all_languages.items():
            if key not in supported_languages:
                unsupported_dict[key] = value
        for key,value in unsupported_dict.items():
            for k in range(0,len(value)):
                if value[k] in text:
                    unexisted+=1
                    unlan.append(key)
                    break
            # if lang_in_text(key,text):
            #     unexisted+=1
            #     unlan.append(key)
            #     break
        print("unlan12",unlan)
        if change_language_count < 1:
            print("existed", existed)
            print("Unexisted",unexisted)
            print("lan182",lan)
            if (existed == 1) and (unexisted >= 1) and (lan == reverse_mapped_languages.get(customer_language,customer_language)):
                existed = 0
            if existed == 0 and unexisted == 0:
                nlu_data_list,count = repeat_verifier(nlu_data_list,requested_slot+"-"+signal)
                if count:
                    return [FollowupAction("action_repeated_utterence"),SlotSet("nlu_data_list_slot", nlu_data_list),]
                print("in existed == 0 and unexisted == 0")
                dispatcher.utter_template(
                "utter_language_change_no_language_"+emi_flow+"_static" + SRP+ bot_gender,tracker,
                languages_integrated=", ".join(supported_languages),supported_languages = supported_languages_1)
                send_and_store_disposition_details(
                    tracker,
                    dispatcher,
                    flag=DEFAULT_FLAG,
                    disposition_details="General - Language Change - Without Language",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"),SlotSet("language_change_with_faq","TRUE"),SlotSet("nlu_data_list_slot", nlu_data_list),]

            if existed >= 1:
                # print("existed >= 1")
                # print("The ln value ",lan)
                # print("lan.lower",lan.lower(),lan)
                # if lan.lower() == "english":
                #     print("lan.lower",lan.lower(),lan)
                #     template_name = "utter_language_change_supported_"+emi_flow+"_static" +bot_gender
                # else:
                #     template_name = "utter_language_change_supported_"+emi_flow+"_static_" + region+ bot_gender
                # print("The generated tempalte in language change",template_name)
                # dispatcher.utter_template(template_name
                #         ,tracker,
                #         language_name=lan)                
                send_and_store_disposition_details(
                    tracker,
                    dispatcher,
                    flag=DEFAULT_FLAG,
                    disposition_details="General - Language Change - Supported",
                    language=lan,
                    emi_flow=emi_flow,
                )
                return [
                    FollowupAction(tracker.active_form.get("name")),
                    SlotSet(REQUESTED_SLOT, None),
                    SlotSet("trail_count", None),
                    FollowupAction(tracker.active_form.get("name")),
                    SlotSet("change_specific_language_count",change_specific_language_count + 1),
                    SlotSet("change_language_count", change_language_count + 1),
                    SlotSet("customer_language_slot", lan),
                    SlotSet("language_change_with_faq", None),
                ]
            elif unexisted >= 1:
                print("unexisted >= 1")
                dispatcher.utter_template("utter_language_change_not_supported_"+emi_flow+"_static"+SRP+bot_gender, # to change back to emi_flow insted of predue
                                tracker,languages_integrated=", ".join(supported_languages),supported_languages = supported_languages_1)
                send_and_store_disposition_details(
                        tracker,
                        dispatcher,
                        flag=TIMEOUT_FLAG,
                        disposition_details="General - Language Change - Not Supported",
                        language=language,
                        emi_flow=language,
                    )
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            print("language-else")
            dispatcher.utter_template("utter_language_change_not_supported_"+emi_flow+"_static"+SRP+bot_gender, # to change back to emi_flow insted of predue
                                tracker,languages_integrated=", ".join(supported_languages),supported_languages = supported_languages_1)
            send_and_store_disposition_details(
                tracker,
                dispatcher,
                flag=TIMEOUT_FLAG,
                disposition_details="General - Language Change - Not Supported",  ##dispo
                language=language,
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]

class ActionDefault(Action):
    def name(self):
        return "action_default"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        print("customer_language212543",customer_language)
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        default_count = tracker.get_slot("default_count")
        account_name = tracker.get_slot("account_name_slot")
        gender = tracker.get_slot("gender_slot")
        slot = tracker.get_slot(REQUESTED_SLOT)
        nlu_data_list = tracker.get_slot("nlu_data_list_slot")
        print(default_count, "default_count-1")
        print("Entering into defualt comment")
        try:
            signal = tracker.latest_message.get("signal").get("name")
        except:
            signal = tracker.latest_message.get("intent").get("name")
        nlu_data_list,count = repeat_verifier(nlu_data_list,slot+"-"+signal)
        print("mpe_nlu_data_list",nlu_data_list)
        if count:
            print("repeeet")
            return [FollowupAction("action_repeated_utterence"),
                    SlotSet("nlu_data_list_slot", nlu_data_list)]
        if default_count < 2:
            if (account_name == "Ring" or account_name == "Ring Testing"):
                if default_count == 0:
                    dispatcher.utter_template(
                        "utter_gibberish_a_"+emi_flow+"_static" + SRP + bot_gender, tracker
                    )
                else:
                    dispatcher.utter_template(
                        "utter_gibberish_b_"+emi_flow+"_static" + SRP + bot_gender, tracker
                    )
            else:
                dispatcher.utter_template(
                    "utter_gibberish_b_"+emi_flow+"_static" + SRP + bot_gender, tracker
                )
            send_and_store_disposition_details(
                tracker = tracker,
                dispatcher = dispatcher,
                flag=DEFAULT_FLAG,
                disposition_details="NLU Low Confidence",
                emi_flow=emi_flow,
            )
            return [
                SlotSet(REQUESTED_SLOT, None),
                SlotSet("trail_count", get_trail_count(tracker)),
                FollowupAction(tracker.active_form.get("name")),
                SlotSet("default_count", default_count + 1),
            ]
        else:
            dispatcher.utter_template("utter_talk_to_human_"+emi_flow+"_static" + SRP + bot_gender, tracker)
            send_and_store_disposition_details(
                tracker,
                dispatcher,
                flag=check_human_handoff_flag(tracker),
                disposition_id="Human Handoff Requested",
                disposition_details=check_human_handoff_details(tracker),
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]

class ActionNoMessage(Action):
    def name(self):
        return "action_no_message"

    def run(self, dispatcher, tracker, domain):
        emi_flow=tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        SRP = SRP_value(customer_language,region)
        account_name = tracker.get_slot("account_name_slot")
        no_response_count = tracker.get_slot("no_response_count")
        language_change_with_faq = tracker.get_slot("language_change_with_faq")
        print("no_response_count",no_response_count)
        latest_event = tracker.events
        previous_message_no_message = True
        user_message_flag = False
        for event in reversed(latest_event):
            if event["event"] == "user":
                if user_message_flag:
                    if event["text"] == "/no_message":
                        previous_message_no_message = False
                        break
                    else:
                        break
                if event["text"] == "/no_message":
                    user_message_flag = True
                    continue
                elif event["text"] == "/noise":
                    no_response_count = None
                    break
        if language_change_with_faq == "TRUE":
            if (no_response_count == None) or (no_response_count<2):
                print("coming here",no_response_count)
                template = "utter_reply_greaterthan_5sec_"+emi_flow+"_static"+SRP+bot_gender
                dispatcher.utter_template(template, tracker)
                send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        user_message="no_message",
                        flag=DEFAULT_FLAG,
                        disposition_details="General - No Message",
                        emi_flow=emi_flow
                    )
                return [FollowupAction("action_change_language"),
                    SlotSet("no_response_count", int(no_response_count) + 1)]
            else:
                dispatcher.utter_template(
                    "utter_disconnect_call_"+emi_flow+"_static"
                    +SRP
                    + bot_gender,
                    tracker,
                )
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    user_message="no_message",
                    flag=TIMEOUT_FLAG,
                    disposition_details="General - Hear Capability - Fail",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]

        if previous_message_no_message:
            no_response_count = None
        print("No Response count:",no_response_count)
        if no_response_count is None:
            if tracker.active_form.get("name") is not None:
                template = "utter_reply_greaterthan_5sec_"+emi_flow+"_static" + SRP + bot_gender
                dispatcher.utter_template(template, tracker)
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    user_message="no_message",
                    flag=DEFAULT_FLAG,
                    disposition_details="General - No Message",
                    emi_flow=emi_flow
                )
                return [
                    SlotSet(REQUESTED_SLOT, None),
                    SlotSet("trail_count", get_trail_count(tracker)),
                    FollowupAction(tracker.active_form.get("name")),
                    SlotSet("no_response_count", 1)
                ]
            template = "utter_reply_greaterthan_5sec_"+emi_flow+"_static" + SRP + bot_gender
            dispatcher.utter_template(template, tracker)
            send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    user_message="no_message",
                    flag=DEFAULT_FLAG,
                    disposition_details="General - No Message",
                    emi_flow=emi_flow,
                )
            return [FollowupAction("action_listen"), SlotSet("no_response_count", 1)]
        else:
            if no_response_count >= 2:
                dispatcher.utter_template(
                    "utter_disconnect_call_"+emi_flow+"_static"
                    +SRP
                    + bot_gender,
                    tracker,
                )
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    user_message="no_message",
                    flag=TIMEOUT_FLAG,
                    disposition_details="General - Hear Capability - Fail",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
            else:
                if tracker.active_form.get("name") is not None:
                    if (account_name == "Ring" or account_name == "Ring Testing"):
                        dispatcher.utter_template(
                            "utter_reply_greaterthan_5sec_b_"+emi_flow+"_static" + SRP + bot_gender,
                            tracker,
                            )
                    else:
                        dispatcher.utter_template(
                            "utter_reply_greaterthan_5sec_"+emi_flow+"_static" + SRP + bot_gender,
                            tracker,
                        )
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details="General - No Response",
                        emi_flow=emi_flow,
                    )
                    return [
                        SlotSet(REQUESTED_SLOT, None),
                        SlotSet("trail_count", get_trail_count(tracker)),
                        FollowupAction(tracker.active_form.get("name")),
                        SlotSet("no_response_count", int(no_response_count) + 1),
                    ]
                if (account_name == "Ring" or account_name == "Ring Testing"):
                    dispatcher.utter_template(
                        "utter_reply_greaterthan_5sec_b_"+emi_flow+"_static" + SRP + bot_gender,
                        tracker,
                        )
                else:
                    dispatcher.utter_template(
                        "utter_reply_greaterthan_5sec_"+emi_flow+"_static" + SRP + bot_gender, tracker
                    )
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    disposition_details="General - No Response",
                    emi_flow=emi_flow,
                )
                return [
                    FollowupAction("action_listen"),
                    SlotSet("no_response_count", int(no_response_count) + 1),
                ]
            
class ActionNoWaitResponse(Action):
    def name(self):
        return "action_no_wait_response"

    def run(self, dispatcher, tracker, domain):
        emi_flow=tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        SRP = SRP_value(customer_language,region)
        wait_no_count = tracker.get_slot("wait_no_count")
        latest_event = tracker.events
        previous_message_no_message = True
        user_message_flag = False
        # print("event3333",event["text"])
        for event in reversed(latest_event):
            if event["event"] == "user":
                if user_message_flag:
                    if (event["text"] == "/no_wait_response<nlu_data>") or (event["text"] == "/no_wait_response"):
                        previous_message_no_message = False
                        break
                    else:
                        break
                if (event["text"] == "/no_wait_response<nlu_data>") or (event["text"] == "/no_wait_response"):
                    user_message_flag = True
                    continue
                elif event["text"] == "/noise":
                    wait_no_count = None
                    break

        if previous_message_no_message:
            wait_no_count = None
        # print("No Response count:",no_response_count)
        if wait_no_count is None:
            wait_no_count = 0
            if tracker.active_form.get("name") is not None:
                template = "utter_customer_reply_greaterthan_5sec_"+emi_flow+"_static" + SRP + bot_gender
                dispatcher.utter_template(template, tracker)
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    user_message="no_wait_response",
                    flag=WAIT_FLAG,
                    disposition_details="General - No Message",
                    emi_flow=emi_flow
                )
                return [SlotSet(REQUESTED_SLOT, None),
                    FollowupAction(tracker.active_form.get("name")),
                    SlotSet("trail_count",1),
                    SlotSet("wait_no_count",wait_no_count+1)]
            # return [FollowupAction("action_listen"), SlotSet("no_response_count", 1)]
        else:
            if wait_no_count >= 2:
                dispatcher.utter_template(
                    "utter_disconnect_call_"+emi_flow+"_static"
                    +SRP
                    + bot_gender,
                    tracker,
                )
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    user_message="no_wait_response",
                    flag=TIMEOUT_FLAG,
                    disposition_details="General - Hear Capability - Fail",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
            else:
                if tracker.active_form.get("name") is not None:
                    dispatcher.utter_template(
                        "utter_customer_reply_greaterthan_5sec_"+emi_flow+"_static" + SRP + bot_gender,
                        tracker,
                    )
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        flag=WAIT_FLAG,
                        disposition_details="General - No Response",
                        emi_flow=emi_flow,
                    )
                    return [SlotSet(REQUESTED_SLOT, None),
                        FollowupAction(tracker.active_form.get("name")),
                        SlotSet("trail_count",1),
                        SlotSet("wait_no_count",wait_no_count+1)]
                # return [
                #     FollowupAction("action_listen"),
                #     SlotSet("no_response_count", int(no_response_count) + 1),
                # ]

class ActionRepeat(Action):
    def name(self):
        return 'action_repeat'

    def run(self,dispatcher,tracker,domain):
        emi_flow=tracker.get_slot("emi_flow")
        repeat_count=int(tracker.get_slot("repeat_count"))
        signal = tracker.latest_message.get("signal").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        print("sdfo33shfsoh")
        if repeat_count<2:
            template  = (
            "utter_speak_clear_"+emi_flow+"_static"+SRP+bot_gender
            )
            dispatcher.utter_template(template,tracker)
            send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,disposition_details="General - Repeat",emi_flow=emi_flow)
            return [
                    SlotSet(REQUESTED_SLOT, None),
                    FollowupAction(tracker.active_form.get("name")),
                    SlotSet("repeat_count",repeat_count+1),
                    SlotSet("trail_count",None),
                    ]
        else:
            print("sdfoshfsoh")
            dispatcher.utter_template(
            "utter_threshold_lessthan_2_"+emi_flow+"_static" + SRP + bot_gender,tracker
            )
            send_and_store_disposition_details(tracker=tracker,flag=TIMEOUT_FLAG,dispatcher=dispatcher,disposition_details="General - Repeat",emi_flow=emi_flow)
            return [FollowupAction("action_listen"), AllSlotsReset()]
        
class ActionLoanCancelled(Action):
    def name(self):
        return "action_loan_cancelled"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        signal = tracker.latest_message.get("signal").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        gender = tracker.get_slot("gender_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        bot_gender = tracker.get_slot("bot_gender")
        late_fees = tracker.get_slot("late_fee_percentage_slot")
        # intent = tracker.latest_message.get("temp_intent").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        # due_date = tracker.get_slot("due_date_without_formatting_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        dispatcher.utter_template(
                "utter_loan_cancelled_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
        send_and_store_disposition_details(
                    tracker=tracker, dispatcher=dispatcher, flag=TIMEOUT_FLAG,disposition_details="General - Loan Cancelled",disposition_id = "Dispute"
                )
        return [FollowupAction("action_listen")]
    
class ActionNotAppliedForLoan(Action):
    def name(self):
        return "action_not_applied_for_loan"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        signal = tracker.latest_message.get("signal").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        gender = tracker.get_slot("gender_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        bot_gender = tracker.get_slot("bot_gender")
        late_fees = tracker.get_slot("late_fee_percentage_slot")
        # intent = tracker.latest_message.get("temp_intent").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        # due_date = tracker.get_slot("due_date_without_formatting_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        dispatcher.utter_template(
                "utter_not_applied_for_loan_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
        send_and_store_disposition_details(
                    tracker=tracker, dispatcher=dispatcher, flag=TIMEOUT_FLAG,disposition_details="General - Never Applied for Loan",disposition_id="Dispute"
                )
        return [FollowupAction("action_listen")]
    
class ActionLoanNotDisbursed(Action):
    def name(self):
        return "action_loan_not_disbursed"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        signal = tracker.latest_message.get("signal").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        gender = tracker.get_slot("gender_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        bot_gender = tracker.get_slot("bot_gender")
        late_fees = tracker.get_slot("late_fee_percentage_slot")
        # intent = tracker.latest_message.get("temp_intent").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        # due_date = tracker.get_slot("due_date_without_formatting_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        dispatcher.utter_template(
                "utter_loan_not_disbursed_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
        send_and_store_disposition_details(
                    tracker=tracker, dispatcher=dispatcher, flag=TIMEOUT_FLAG,disposition_details="General - Loan Not Disbursed",disposition_id = "Dispute"
                )
        return [FollowupAction("action_listen")]
        

class ActionLateFees(Action):
    def name(self):
        return "action_late_fees"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        signal = tracker.latest_message.get("signal").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        gender = tracker.get_slot("gender_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        bot_gender = tracker.get_slot("bot_gender")
        late_fees = tracker.get_slot("late_fee_percentage_slot")
        # intent = tracker.latest_message.get("temp_intent").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        # due_date = tracker.get_slot("due_date_without_formatting_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)

        if late_fees == "":
            dispatcher.utter_template(
                "utter_quantitative_data_alt_response_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
            send_and_store_disposition_details(
                    tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG,disposition_details="General - Pay Late Fee"
                )
            return get_return_values(tracker)
            
        else:
            if signal == "late_fees" and (sub_context == "quantitative_data" or sub_context == "action_by_bot"):
                dispatcher.utter_template(
                    "utter_quantitative_data_late_fees_PTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender,
                    tracker,
                    late_fee_percentage=late_fees,
                )
                if len(entities) == 0:
                    print("Entering into IF")
                    if tracker.active_form.get("name") is not None:
                        send_and_store_disposition_details(
                                        tracker=tracker,dispatcher=dispatcher,
                                        disposition_details=intent.capitalize()+" Late Fees",
                                        flag=DEFAULT_FLAG,
                                    )
                        return get_return_values(tracker)
                    return [FollowupAction("action_listen")]
                else:
                    for entity in entities:
                        date_condition = False
                        given_date = ""
                        if entity.get("entity", None) == "date":
                            due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                            if "due_date" in entity["value"]:
                                value = entity["value"].split("due_date")[1]
                                if "-" in value:
                                    value  = value.split("-")[1]
                                    given_date = due_date - timedelta(days=int(value))
                                elif "+" in value:
                                    value = value.split("+")[1]
                                    given_date = due_date + timedelta(days=int(value))
                                else:
                                    given_date =  due_date
                            else:
                                given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                            if emi_flow == "predue":
                                date_condition = (given_date.date()<= due_date.date())
                            else:
                                no_of_days = given_date.date() - datetime.datetime.now().date()
                                date_condition = (no_of_days.days <= int(threshold_days))
                            given_date = given_date.strftime("%d %B %Y").lstrip('0')
                        for entity in entities:
                            if entity.get("entity", None) == "time":
                                th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                                given_time = entity["value"]
                                th_ptp_time1 = th_ptp_time.split(":")
                                given_date_time = given_date + given_time
                                given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                                print("the given_date_time",given_date_time)
                                if emi_flow == "predue":
                                    th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                                else:
                                    today = datetime.datetime.now()
                                    atp_date = today + timedelta(days=int(threshold_days))
                                    th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                                date_condition = (given_date_time <= th_date_time)
                        if date_condition:
                            # dispatcher.utter_template("utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker)
                            send_and_store_disposition_details(
                                tracker=tracker,dispatcher=dispatcher,
                                disposition_details=intent.capitalize()+" Late Fees",disposition_id="APTP",
                                flag=DEFAULT_FLAG,
                            )
                            return aptp_decide_slot(tracker)
                        else:
                            if tracker.active_form.get("name") is not None:
                                send_and_store_disposition_details(tracker=tracker,
                                dispatcher=dispatcher,disposition_details=intent.capitalize()+" Late Fees",disposition_id="UPTP",flag=DEFAULT_FLAG)
                                return decide_slot(tracker)
                    return get_return_values(tracker)
            else:
                send_and_store_disposition_details(tracker=tracker,
                                    dispatcher=dispatcher,flag=DEFAULT_FLAG)
                return get_return_values(tracker)

class ActionWhoAreYou(Action):
    def name(self):
        return "action_who_are_you"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        clinet_name = tracker.get_slot("client_name_slot")
        bank_name = tracker.get_slot("bank_name_slot")
        agent_name = tracker.get_slot("agent_name")
        dispatcher.utter_template(
            "utter_general_who_are_you_"+emi_flow+"_static" + SRP + bot_gender,
            tracker,
            client_name=bank_name,
            agent_name=agent_name,
        )
        send_and_store_disposition_details(
            tracker=tracker,
            dispatcher=dispatcher,
            disposition_details="General - Agent Identification",
            flag=DEFAULT_FLAG,
            emi_flow=emi_flow,
        )
        return get_return_values(tracker)


class ActionAreYouThere(Action):
    def name(self):
        return "action_are_you_there"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        are_you_there_count = tracker.get_slot("are_you_there_count")
        if are_you_there_count <2:
            if signal == "are_you_there":
                dispatcher.utter_template(
                    "utter_general_are_you_there_"+emi_flow+"_static" + SRP + bot_gender, tracker
                )
            send_and_store_disposition_details(
                tracker=tracker,
                dispatcher=dispatcher,
                disposition_details="General - Reconfirmation",
                flag=DEFAULT_FLAG,
                emi_flow=emi_flow,
            )
            return get_return_values(tracker) + [
                SlotSet("are_you_there_count",are_you_there_count+1)
            ]
        else:
            dispatcher.utter_template(
            "utter_threshold_lessthan_2_"+emi_flow+"_static" + SRP + bot_gender,tracker
            )
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="General - Hear Capability - Fail",              ##dispo
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        
class ActionBotHumiliate(Action):
    def name(self):
        return "action_bot_humiliation"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        humiliate_count=int(tracker.get_slot("humiliate_count"))
        print("coming hereeerer")
        if humiliate_count <2:
            dispatcher.utter_template(
                    "utter_gibberish_a_"+emi_flow+"_static" + SRP + bot_gender, tracker
                )
            send_and_store_disposition_details(
            tracker=tracker,
            dispatcher=dispatcher,
            disposition_details="General - Humiliate",
            flag=DEFAULT_FLAG,
            emi_flow=emi_flow,
        )
        else:
            dispatcher.utter_template(
            "utter_threshold_lessthan_2_"+emi_flow+"_static" + SRP + bot_gender,tracker
        )
            send_and_store_disposition_details(
                tracker=tracker,
                dispatcher=dispatcher,
                disposition_details="General - Humiliate",
                flag=TIMEOUT_FLAG,
                emi_flow=emi_flow,
            )
        return [FollowupAction("action_listen"),SlotSet("humiliate_count",humiliate_count+1)]

class ActionThankYOu(Action):
    def name(self):
        return "action_thank_you"
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        thank_you_count = tracker.get_slot("thank_you_count")
        print("coming hereeerer")
        if thank_you_count < 2:
            dispatcher.utter_template(
                    "utter_gibberish_a_"+emi_flow+"_static" + SRP + bot_gender, tracker
                )
            send_and_store_disposition_details(
                tracker=tracker,
                dispatcher=dispatcher,
                disposition_details="General - Thankyou",
                flag=DEFAULT_FLAG,
                emi_flow=emi_flow,
            )
            return get_return_values(tracker) + [
                SlotSet("thank_you_count", thank_you_count + 1)
            ]
        else:
            dispatcher.utter_template(
            "utter_threshold_lessthan_2_"+emi_flow+"_static" + SRP + bot_gender,tracker
            )
            send_and_store_disposition_details(tracker=tracker,flag=TIMEOUT_FLAG,dispatcher=dispatcher,disposition_details="General - Repeat",emi_flow=emi_flow)
            return [FollowupAction("action_listen"), AllSlotsReset()]

class ActionBye(Action):
    def name(self):
        return "action_bye"
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        bye_count = tracker.get_slot("bye_count")
        print("coming hereeerer")
        if bye_count < 2:
            dispatcher.utter_template(
                    "utter_gibberish_a_"+emi_flow+"_static" + SRP + bot_gender, tracker
                )
            send_and_store_disposition_details(
                tracker=tracker,
                dispatcher=dispatcher,
                disposition_details="General - Bye",
                flag=DEFAULT_FLAG,
                emi_flow=emi_flow,
            )
            return get_return_values(tracker) + [
                SlotSet("bye_count", bye_count + 1)
            ]
        else:
            dispatcher.utter_template(
            "utter_threshold_lessthan_2_"+emi_flow+"_static" + SRP + bot_gender,tracker
            )
            send_and_store_disposition_details(tracker=tracker,flag=TIMEOUT_FLAG,dispatcher=dispatcher,disposition_details="General - Repeat",emi_flow=emi_flow)
            return [FollowupAction("action_listen"), AllSlotsReset()]

class ActionBankAccountRelated(Action):
    def name(self):
        return "action_bank_account_related"
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        # SRP = tracker.get_slot("SRP_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        dispatcher.utter_template(
            "utter_action_by_client_noPTPdate_"+emi_flow+"_static" + SRP + bot_gender, tracker)
        send_and_store_disposition_details(
            tracker=tracker,
            dispatcher=dispatcher,
            disposition_details="General - Bank Account Related Issue",
            flag=TIMEOUT_FLAG,
            emi_flow=emi_flow,
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]

class ActionForeclosing(Action):
    def name(self):
        return "action_foreclosing_through_own_funds"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        intent = tracker.latest_message.get("temp_intent").get("name")
        threshold_days = tracker.get_slot("threshold_days_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        partial_payment = tracker.get_slot("partial_payment_slot")
        partial_payment_stage_slot = tracker.get_slot("Partial_payment_stage_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        minimum_pp_emi_amount = tracker.get_slot("minimum_pp_emi_amount_slot")
        maximum_pp_emi_amount = tracker.get_slot("maximum_pp_emi_amount_slot")
        emi_amount = tracker.get_slot("emi_amount_slot")
        print("entities1233",entities)
        dispatcher.utter_template(
            "utter_action_by_client_noPTPdate_"+emi_flow+"_static" + SRP + bot_gender, tracker
        )
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Foreclosing with own funds",
                    flag=DEFAULT_FLAG,
                    emi_flow=emi_flow)
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            print("comfijf")
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                        if date_condition:
                            # dispatcher.utter_template(
                            #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                            # )
                            print("Entering into AccPTP")
                            send_and_store_disposition_details(
                                tracker=tracker,
                                dispatcher=dispatcher,
                                disposition_details=intent.capitalize()+" Foreclosing with own funds",disposition_id="APTP",
                                ptp_date=given_date,
                                flag=DEFAULT_FLAG,
                                emi_flow=emi_flow)
                            return aptp_decide_slot(tracker)
                        else:
                            if tracker.active_form.get("name") is not None:
                                print("Entering into Not AccPTP")
                                send_and_store_disposition_details(
                                        tracker=tracker,
                                        dispatcher=dispatcher,
                                        disposition_details=intent.capitalize()+" Foreclosing with own funds",disposition_id="UPTP",
                                        ptp_date=given_date,
                                        flag=DEFAULT_FLAG,
                                        emi_flow=emi_flow)
                                return decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                                tracker=tracker,
                                dispatcher=dispatcher,
                                disposition_details=intent.capitalize()+" Foreclosing with own funds",
                                flag=DEFAULT_FLAG,
                                emi_flow=emi_flow)
                        return decide_slot(tracker)
                # if entity.get("entity", None) == "number":
                #     given_amount = int(entity["value"])
                #     if partial_payment != "yes":
                #         amount_condition = (given_amount >= int(emi_amount))
                #     else:
                #         print("mpe1465")
                #         if level_of_negotiation == "1":
                #             amount_condition = (given_amount >= int(minimum_pp_emi_amount))
                #         if level_of_negotiation == "2":
                #             amount_condition = (given_amount >= int(maximum_pp_emi_amount))
                
                # else:
                #     print("Entering into NoPTP with other entities")
                #     return get_return_values(tracker)
            return [FollowupAction("action_listen")]


class ActionChangeAccount(Action):
    def name(self):
        return "action_change_account_for_deduction"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        intent = tracker.latest_message.get("temp_intent").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        dispatcher.utter_template(
            "utter_action_by_client_noPTPdate_"+emi_flow+"_static" + SRP + bot_gender, tracker)
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Change account for deduction",
                    flag=DEFAULT_FLAG,
                    emi_flow=emi_flow)
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Change account for deduction",disposition_id="APTP",
                        ptp_date= given_date,
                        flag=DEFAULT_FLAG,
                        emi_flow=emi_flow
                        )
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Change account for deduction",disposition_id="UPTP",
                            ptp_date = given_date,
                            flag=DEFAULT_FLAG,
                            emi_flow=emi_flow
                        )
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class MoratoriumPeriod(Action):
    def name(self):
        return "action_moratorium_period"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        intent = tracker.latest_message.get("temp_intent").get("name")
        threshold_days = tracker.get_slot("threshold_days_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        dispatcher.utter_template(
            "utter_action_by_client_noPTPdate_"+emi_flow+"_static" + SRP + bot_gender, tracker
        )
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Moratorium Period",
                    flag=DEFAULT_FLAG,
                    emi_flow=emi_flow,)
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker)
                    # print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Moratorium Period",disposition_id="APTP",
                        ptp_date=given_date,
                        flag=DEFAULT_FLAG,
                        emi_flow=emi_flow)
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Moratorium Period",disposition_id="UPTP",
                            ptp_date=given_date,
                            flag=DEFAULT_FLAG,
                            emi_flow=emi_flow)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class ChangeEmiDate(Action):
    def name(self):
        return "action_change_emi_due_date"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        intent = tracker.latest_message.get("temp_intent").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        dispatcher.utter_template(
            "utter_action_by_client_noPTPdate_"+emi_flow+"_static" + SRP + bot_gender, tracker
        )
        if len(entities) == 0 or len(entities) > 0:
            print("Entering into NoPTP")
            send_and_store_disposition_details(
                tracker=tracker,
                dispatcher=dispatcher,
                disposition_details=intent.capitalize()+" Change EMI date",
                flag=DEFAULT_FLAG,
                emi_flow=emi_flow)
            return get_return_values(tracker)
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    # print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Change EMI date",disposition_id="APTP",
                        ptp_date = given_date,
                        flag=DEFAULT_FLAG,
                        emi_flow=emi_flow)
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Change EMI date",disposition_id="UPTP",
                            ptp_date = given_date,
                            flag=DEFAULT_FLAG,
                            emi_flow=emi_flow)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class ReduceEmi(Action):
    def name(self):
        return "action_reduce_emi"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        intent = tracker.latest_message.get("temp_intent").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        dispatcher.utter_template(
            "utter_action_by_client_noPTPdate_"+emi_flow+"_static" + SRP + bot_gender, tracker
        )
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Reduce EMI",
                    flag=DEFAULT_FLAG,
                    emi_flow=emi_flow)
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    # print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Reduce EMI",disposition_id="APTP",
                        ptp_date = given_date,
                        flag=DEFAULT_FLAG,
                        emi_flow=emi_flow)
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Reduce EMI",disposition_id="UPTP",
                            ptp_date = given_date,
                            flag=DEFAULT_FLAG,
                            emi_flow=emi_flow)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]

class ActionInformPaymentDone(Action):
    def name(self):
        return "action_inform_payment_done"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        entities = tracker.latest_message["entities"]
        SRP = SRP_value(customer_language,region)
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        # intent = tracker.latest_message.get("temp_intent").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        print("The value of signal ****", signal)
        print("The value of sentiment *****", sentiment)
        if (
            (signal == "payment_done")
            and (context == "payment" or context == "general" or context == "loan")
        ):
            if sentiment == "positive" or sentiment == "neutral":
                template = (
                    "utter_payment_done_positive_"+emi_flow+"_static" + SRP + bot_gender
                )
            elif sentiment == "negative":
                template = (
                    "utter_payment_done_negative_"+emi_flow+"_static" + SRP + bot_gender
                )
            print("The generated template on payment done", template)
            dispatcher.utter_template(template, tracker)
            disposition_="UCP"
            if entities:
                for entity in entities:
                    if entity.get("entity", None) == "date":
                        disposition_ = "UCPPD"
            send_and_store_disposition_details(
                tracker=tracker,
                dispatcher=dispatcher,
                disposition_id=disposition_, #User Claimed Payment
                flag=TIMEOUT_FLAG,
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            send_and_store_disposition_details(tracker=tracker,
                                dispatcher=dispatcher,flag=DEFAULT_FLAG)
            return get_return_values(tracker)


class ActionAskEmiAmount(Action):
    def name(self):
        return "ask_emi_amount"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        emi_amount = tracker.get_slot("emi_amount_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        threshold_days = tracker.get_slot("threshold_days_slot")
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        # intent = tracker.latest_message.get("temp_intent").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        entities = tracker.latest_message["entities"]
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        emi_amount = tracker.get_slot("emi_amount_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        if (signal == "emi_amount") and (sub_context == "issue"):
            template = (
            "utter_issue_customer_or_account_details_"+emi_flow+"_static" + SRP + bot_gender
        )
            dispatcher.utter_template(template, tracker, monthly_emi=emi_amount)
            send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" EMI Amount",
                    flag=TIMEOUT_FLAG,
                    emi_flow=emi_flow)
            
            return [FollowupAction("action_listen")]
        else:
            template = (
                "utter_action_by_bot_emi_amount_noPTPdate_"+emi_flow+"_static" + SRP + bot_gender
            )
            print("The generate template is ", template)
            dispatcher.utter_template(template, tracker, monthly_emi=emi_amount)
            if len(entities) == 0:
                print("Entering into NoPTP")
                if tracker.active_form.get("name") is not None:
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" EMI Amount",
                        flag=DEFAULT_FLAG,
                        emi_flow=emi_flow)
                    return get_return_values(tracker)
                    
                return [FollowupAction("action_listen")]
            else:
                for entity in entities:
                    date_condition = False
                    given_date = ""
                    if entity.get("entity", None) == "date":
                        due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                        if "due_date" in entity["value"]:
                            value = entity["value"].split("due_date")[1]
                            if "-" in value:
                                value  = value.split("-")[1]
                                given_date = due_date - timedelta(days=int(value))
                            elif "+" in value:
                                value = value.split("+")[1]
                                given_date = due_date + timedelta(days=int(value))
                            else:
                                given_date =  due_date
                        else:
                            given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                        if emi_flow == "predue":
                            date_condition = (given_date.date()<= due_date.date())
                        else:
                            no_of_days = given_date.date() - datetime.datetime.now().date()
                            date_condition = (no_of_days.days <= int(threshold_days))
                        given_date = given_date.strftime("%d %B %Y").lstrip('0')
                    for entity in entities:
                        if entity.get("entity", None) == "time":
                            th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                            given_time = entity["value"]
                            th_ptp_time1 = th_ptp_time.split(":")
                            given_date_time = given_date + given_time
                            given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                            print("the given_date_time",given_date_time)
                            if emi_flow == "predue":
                                th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                            else:
                                today = datetime.datetime.now()
                                atp_date = today + timedelta(days=int(threshold_days))
                                th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                            date_condition = (given_date_time <= th_date_time)
                    if date_condition:
                        # dispatcher.utter_template(
                        #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                        # )
                        print("Entering into AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" EMI Amount",disposition_id="APTP",
                            ptp_date = given_date,
                            flag=DEFAULT_FLAG,
                            emi_flow=emi_flow)
                        return aptp_decide_slot(tracker)
                    else:
                        if tracker.active_form.get("name") is not None:
                            print("Entering into Not AccPTP")
                            send_and_store_disposition_details(
                                tracker=tracker,
                                dispatcher=dispatcher,
                                disposition_details=intent.capitalize()+" EMI Amount",disposition_id="UPTP",
                                ptp_date = given_date,
                                flag=DEFAULT_FLAG,
                                emi_flow=emi_flow)
                            return decide_slot(tracker)
                return [FollowupAction("action_listen")]


class ActionAskDueDate(Action):
    def name(self):
        return "action_ask_emi_due_date"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        due_date = tracker.get_slot("due_date")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        context = tracker.latest_message.get("context").get("name")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        variation = tracker.get_slot("variation_slot")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")

        if signal == "emi_due_date" and (sub_context == "quantitative_data" or sub_context == "action_by_bot"):
            print("Enterint into IF of ask due date")
            dispatcher.utter_template(
                "utter_quantitative_data_emi_due_date_PTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker,
                monthly_emi_date=due_date,
            )
            send_and_store_disposition_details(
                tracker=tracker,
                flag=DEFAULT_FLAG,
                dispatcher=dispatcher,
                disposition_details=intent.capitalize()+" EMI Due Date",
                emi_flow=emi_flow,
            )
            return get_return_values(tracker)
        elif signal == "emi_due_date" and (sub_context == "issue"):
            print("Enterint into IF of ask due date")
            dispatcher.utter_template(
                "utter_issue_customer_or_account_details_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker,
                monthly_emi_date=due_date,
            )
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="General - Inform Issue",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        elif len(entities) == 0 or len(entities) > 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" EMI Due Date",
                    flag=DEFAULT_FLAG,
                    emi_flow=emi_flow)
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        elif len(entities)<0:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" EMI Due Date",disposition_id="APTP",
                        ptp_date = given_date,
                        flag=DEFAULT_FLAG,
                        emi_flow=emi_flow)
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" EMI Due Date",disposition_id="UPTP",
                            ptp_date= given_date,
                            flag=DEFAULT_FLAG,
                            emi_flow=emi_flow)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]
        elif delay_reason_needed == "yes":
            if delay_reason == "emi_date_not_informed":
                dispatcher.utter_template(
                    "utter_emi_date_not_confirmed_"+variation+emi_flow+"_"
                    + region
                    + gender
                    + age_category
                    + collared
                    + "_"
                    + typology
                    + bot_gender,
                    tracker,
                )
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Date Not Informed",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]
        


class ActionAskNextDueDate(Action):
    def name(self):
        return "action_ask_next_due_date"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        user_message = tracker.latest_message.get("text")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        print("cojfjf")
        if signal == "next_due_date" and (sub_context == "quantitative_data" or sub_context == "action_by_bot"):
            dispatcher.utter_template(
                "utter_quantitative_data_next_due_date_PTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker,
            )
        if len(entities) == 0 or len(entities) > 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    user_message=user_message,
                    disposition_details=intent.capitalize()+" Next Due Date",
                    flag=DEFAULT_FLAG,
                    emi_flow=emi_flow)
                print('hahd')
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                        # dispatcher.utter_template(
                        #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                        # )
                        # print("Entering into AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            user_message=user_message,
                            disposition_details=intent.capitalize()+" Next Due Date",disposition_id="APTP",
                            ptp_date=given_date,
                            flag=DEFAULT_FLAG,
                            emi_flow=emi_flow)
                        return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            user_message=user_message,
                            disposition_details=intent.capitalize()+" Next Due Date",disposition_id="UPTP",
                            ptp_date=given_date,
                            flag=DEFAULT_FLAG,
                            emi_flow=emi_flow)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class ActionPrinciapalAmount(Action):
    def name(self):
        return "action_principal_amount"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        bot_gender = tracker.get_slot("bot_gender")
        gender = tracker.get_slot("gender_slot")
        principal_amount = tracker.get_slot("principal_amount_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)

        if signal == "principal_amount" and (sub_context == "quantitative_data" or sub_context == "action_by_bot") and principal_amount !="":
            dispatcher.utter_template(
                "utter_action_by_bot_principal_amount_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker,
                principal_amount=principal_amount,
            )
        else:
            dispatcher.utter_template(
                "utter_quantitative_data_alt_response_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
        print("fdf",len(entities))
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Principal Amount",
                    emi_flow=emi_flow,)
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    # print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        flag=DEFAULT_FLAG,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Principal Amount",disposition_id="APTP",
                        ptp_date= given_date,
                        emi_flow=emi_flow,)
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            flag=DEFAULT_FLAG,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Principal Amount",disposition_id="UPTP",
                            ptp_date= given_date,
                            emi_flow=emi_flow,)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class ActionLoanStartDate(Action):
    def name(self):
        return "action_loan_start_date"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        loan_start_date = tracker.get_slot("loan_start_date_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        intent = tracker.latest_message.get("temp_intent").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        if loan_start_date != "":
            loan_start_date = datetime.datetime.strptime(loan_start_date, "%d-%m-%Y")
            print("loan_start_date123",loan_start_date)
            loan_start_date = loan_start_date.strftime("%d %B %Y").lstrip('0')
            print("loan_start_date321",loan_start_date)
            dispatcher.utter_template(
                "utter_action_by_bot_loan_start_date_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker,
                loan_start_date=loan_start_date,
            )
        else:
            dispatcher.utter_template(
                "utter_quantitative_data_alt_response_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Loan Start Date",
                    emi_flow=emi_flow,)
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    # print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        flag=DEFAULT_FLAG,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Loan Start Date",disposition_id="APTP",
                        ptp_date= given_date,
                        emi_flow=emi_flow,)
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            flag=DEFAULT_FLAG,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Loan Start Date",disposition_id="UPTP",
                            ptp_date=given_date,
                            emi_flow=emi_flow,)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class ActionHowAreYou(Action):
    def name(self):
        return "action_how_are_you"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        loan_start_date = tracker.get_slot("loan_start_date_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        if loan_start_date != "":
            loan_start_date = datetime.datetime.strptime(loan_start_date, "%d-%m-%Y").strftime("%d %B ").lstrip('0')
        dispatcher.utter_template(
            "utter_general_how_are_you_"+emi_flow+"_static" + SRP + bot_gender,
            tracker,
            loan_start_date=loan_start_date,
        )
        send_and_store_disposition_details(
            tracker=tracker,
            flag=DEFAULT_FLAG,
            dispatcher=dispatcher,
            disposition_details="General - Greet",
            emi_flow=emi_flow,
        )
        return get_return_values(tracker)


class ActionTelephoneNetwrokIssue(Action):
    def name(self):
        return "action_telephone_network_issue"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        dispatcher.utter_template(
            "utter_network_problem_"+emi_flow+"_static" + SRP + bot_gender, tracker
        )
        send_and_store_disposition_details(
            tracker=tracker,
            flag=TIMEOUT_FLAG,
            dispatcher=dispatcher,
            disposition_details="General - Network Issue",
            emi_flow=emi_flow,
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]
class ActionHaveBalanceAutodebit(Action):
    def name(self):
        return "action_have_balance_autodebit"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        current_main_slot = tracker.get_slot("current_main_slot")
        payment_method = paymentMode(tracker,"available_payment_mode")
        due_date = tracker.get_slot("due_date_without_formatting_slot")
        partial_payment = tracker.get_slot("partial_payment_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        emi_amount = tracker.get_slot("emi_amount_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        minimum_pp_emi_amount = tracker.get_slot("minimum_pp_emi_amount_slot")
        maximum_pp_emi_amount = tracker.get_slot("maximum_pp_emi_amount_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        entities = tracker.latest_message["entities"]
        print("auto_debit4134",auto_debit)
        print("comingggghhrere",auto_debit)
        if sub_intent == "deny":
            send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            flag=DEFAULT_FLAG,disposition_id="RTP",
                        )
            return decide_slot(tracker)
        if auto_debit == "manual payment":
            dispatcher.utter_template(
                "utter_have_balance_auto_debit_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker,available_payment_mode = payment_method
            )
            send_and_store_disposition_details(
                tracker=tracker,
                flag=DEFAULT_FLAG,
                dispatcher=dispatcher,
                disposition_id="ATP",
                emi_flow=emi_flow,
            )
            return get_return_values(tracker)
        elif auto_debit == "auto debit with manual payment" and sub_intent == "deny":
            send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            flag=DEFAULT_FLAG,disposition_id="RTP",
                        )
            return decide_slot(tracker)
        elif (auto_debit == "auto debit with manual payment") or (auto_debit == "auto debit"):
            if entities:
                for entity in entities:
                    date_condition = amount_condition = True
                    if entity.get("entity", None) == "date":
                        if "due_date" in entity["value"]:
                            value = entity["value"].split("due_date")[1]
                            if "-" in value:
                                value  = value.split("-")[1]
                                date = datetime.datetime.strptime(due_date, "%d-%m-%Y")
                                given_date = date - timedelta(days=int(value))
                            elif "+" in value:
                                value = value.split("+")[1]
                                date = datetime.datetime.strptime(due_date, "%d-%m-%Y")
                                given_date = date + timedelta(days=int(value))
                            else:
                                given_date =  datetime.datetime.strptime(due_date, "%d-%m-%Y")
                        else:
                            given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                        due_date= datetime.datetime.strptime(due_date,"%d-%m-%Y")
                        if emi_flow == "predue":
                            print("the given date",given_date)
                            print("the due_date",due_date)
                            date_condition = (given_date.date()<= due_date.date())
                        else:
                            no_of_days = given_date.date() - datetime.datetime.now().date()
                            print("no_of_days", no_of_days.days)
                            date_condition = (no_of_days.days <= int(threshold_days))
                        given_date = given_date.strftime("%d %B %Y").lstrip('0')
                    for entity in entities:
                        if entity.get("entity", None) == "time":
                            th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                            given_time = entity["value"]
                            th_ptp_time1 = th_ptp_time.split(":")
                            given_date_time = given_date + given_time
                            given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                            print("the given_date_time",given_date_time)
                            if emi_flow == "predue":
                                th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                            else:
                                today = datetime.datetime.now()
                                atp_date = today + timedelta(days=int(threshold_days))
                                th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                            date_condition = (given_date_time <= th_date_time)
                    if entity.get("entity", None) == "number" and int(entity.get("value", None)) > 31:
                        given_amount = int(entity["value"])
                        if partial_payment != "yes":
                            amount_condition = (given_amount >= int(emi_amount))
                        else:
                            print("mpe1465")
                            if level_of_negotiation == "1":
                                amount_condition = (given_amount >= int(minimum_pp_emi_amount))
                            if level_of_negotiation == "2":
                                amount_condition = (given_amount >= int(maximum_pp_emi_amount))
                        print("date_condition,amount_condition: ",date_condition,amount_condition)
                    if date_condition and amount_condition:
                        dispatcher.utter_template("utter_have_balance_autodebit_PTPdate_"+auto_debit_nach+emi_flow+"_static"+SRP+bot_gender,tracker)
                        dispatcher.utter_template("utter_APTP_NACH_"+emi_flow+"_static"+SRP+bot_gender,tracker)
                        send_and_store_disposition_details(
                            tracker=tracker,flag=TIMEOUT_FLAG,dispatcher=dispatcher, disposition_id="APTP",ptp_date=given_date)
                        return [FollowupAction("action_listen"), AllSlotsReset()]
                    elif amount_condition == False:
                        if partial_payment == "no" and emi_flow != "predue" and emi_flow != "due_date":
                            print("inside main response validation")
                            dispatcher.utter_template("utter_partial_payment_not_supported_"+emi_flow+"_static"+SRP+bot_gender,tracker)
                            send_and_store_disposition_details(tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG,
                                disposition_id="Minimum Amount Due Requested",disposition_details="User")
                            return [FollowupAction("action_listen"), AllSlotsReset()]
                        elif (partial_payment == "yes" and partial_payment_count!= "triggered"
                            and emi_flow!="predue" and emi_flow!="duedate"):
                            print("move to pp from slot2")
                            send_and_store_disposition_details(tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG,
                                disposition_id="Minimum Amount Due Requested",disposition_details="User")
                            return [FollowupAction("partial_payment_lvl1_form"), 
                                    SlotSet(REQUESTED_SLOT,None), 
                                    SlotSet("changing_slot",str(current_main_slot)),
                                    SlotSet("trail_count",None),]
                        else:
                            print("The value of entites55",entities)
                            send_and_store_disposition_details(
                                tracker=tracker,dispatcher=dispatcher,flag=DEFAULT_FLAG,disposition_id="RTP")
                            return get_return_values(tracker)
                    else:
                        print("current_main_slot2691",current_main_slot)
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            flag=DEFAULT_FLAG,disposition_id="UPTP",ptp_date = given_date,
                        )
                        return decide_slot(tracker)
            else:
                dispatcher.utter_template(
                "utter_have_balance_autodebit_PTPdate_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker,available_payment_mode = payment_method
            )
                send_and_store_disposition_details(
                        tracker=tracker,dispatcher=dispatcher,flag=TIMEOUT_FLAG,disposition_id="ATP")
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            print("comeerhe")
            dispatcher.utter_template(
                "utter_have_balance_autodebit_PTPdate_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker,available_payment_mode = payment_method
                    #"utter_have_balance_auto_debit_PTPdate_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker,available_payment_mode = payment_method
            )
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_id="APTP",          ##dispo
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]


class ActionLoanEndDate(Action):
    def name(self):
        return "action_loan_end_date"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        loan_end_date = tracker.get_slot("loan_end_date_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        intent = tracker.latest_message.get("temp_intent").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        if loan_end_date != "":
            loan_end_date = datetime.datetime.strptime(loan_end_date, "%d-%m-%Y").strftime("%d %B %Y").lstrip('0')
            dispatcher.utter_template(
                "utter_action_by_bot_loan_end_date_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker,
                loan_end_date=loan_end_date,
            )
        else:
            dispatcher.utter_template(
                "utter_quantitative_data_alt_response_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Loan End Date",
                    emi_flow=emi_flow,
                )
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    # print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        flag=DEFAULT_FLAG,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Loan End Date",disposition_id="APTP",
                        ptp_date = given_date,
                        emi_flow=emi_flow)
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            flag=DEFAULT_FLAG,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Loan End Date",disposition_id="UPTP",
                            ptp_date=given_date,
                            emi_flow=emi_flow
                            )
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class ActionCustomerCareConnect(Action):
    def name(self):
        return "action_customer_care_contact"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        loan_end_date = tracker.get_slot("loan_end_date_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        dispatcher.utter_template(
            "utter_customer_care_contact_"+emi_flow+"_static" + SRP + bot_gender, tracker
        )
        send_and_store_disposition_details(
            tracker=tracker,
            flag=TIMEOUT_FLAG,
            dispatcher=dispatcher,
            disposition_details="General - Customer Care Contact",
            emi_flow=emi_flow,
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]


class ActionTalkToHuman(Action):
    def name(self):
        return "action_talk_to_human"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        agent_desktop = tracker.get_slot("agent_desktop_slot")
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        if agent_desktop == "yes":
            if sub_intent == "general_ask_inform" or sub_intent == "affirm":
                dispatcher.utter_template("utter_affirm_speak_executive_"+emi_flow+"_static"+SRP+bot_gender,tracker)
                send_and_store_disposition_details(
                    tracker=tracker,dispatcher=dispatcher,flag=HANDOFF_FLAG,
                    disposition_id="Human Handoff Requested",disposition_details="Agent Desktop Available")
                return [FollowupAction("action_listen"), AllSlotsReset()]
            else:
                return get_return_values(tracker)
        else:
            dispatcher.utter_template("utter_talk_to_human_"+emi_flow+"_static" + SRP + bot_gender, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_id="Human Handoff Requested",
                disposition_details="Agent Desktop Unavailable",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]


class ActionLoanCancellation(Action):
    def name(self):
        return "action_loan_cancellation"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        dispatcher.utter_template(
            "utter_loan_cancellation_"+emi_flow+"_static" + SRP + bot_gender, tracker
        )
        send_and_store_disposition_details(
            tracker=tracker,
            flag=TIMEOUT_FLAG,
            dispatcher=dispatcher,
            disposition_details="General - Loan Cancellation",
            disposition_id = "Dispute",
            emi_flow=emi_flow,
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]


class ActionNetworkIssue(Action):
    def name(self):
        return "action_telephone_network_issue"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        dispatcher.utter_template(
            "utter_network_problem_"+emi_flow+"_static" + SRP + bot_gender, tracker
        )
        send_and_store_disposition_details(
            tracker=tracker,
            flag=TIMEOUT_FLAG,
            dispatcher=dispatcher,
            disposition_details="General - Network Issue",
            emi_flow=emi_flow,
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]


class ActionTodayDate(Action):
    def name(self):
        return "action_date_today"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        today = datetime.date.today()
        formatted_date = today.strftime('%d %B %Y').lstrip('0')
        SRP = SRP_value(customer_language,region)
        intent = tracker.latest_message.get("temp_intent").get("name")
        dispatcher.utter_template(
            "utter_action_by_bot_today_date_"+emi_flow+"_static" + SRP + bot_gender, tracker, today_date = formatted_date
        )
        send_and_store_disposition_details(
            tracker=tracker,
            flag=DEFAULT_FLAG,
            dispatcher=dispatcher,
            disposition_details=intent.capitalize()+" Today Date",
            emi_flow=emi_flow,
        )
        return get_return_values(tracker)


class ActionLoanAmountRemaining(Action):
    def name(self):
        return "action_loan_amount_remaining"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        loan_amount_remaining = tracker.get_slot("loan_amount_remaining_slot")
        entities = tracker.latest_message["entities"]
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        intent = tracker.latest_message.get("temp_intent").get("name")
        SRP = SRP_value(customer_language,region)
        threshold_days = tracker.get_slot("threshold_days_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        if loan_amount_remaining != "":
            dispatcher.utter_template(
                "utter_action_by_bot_loan_remaining_amount_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker,
                loan_remaining_amount=loan_amount_remaining,
            )
        else:
            dispatcher.utter_template(
                "utter_quantitative_data_alt_response_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
        
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+ " Loan Amount",
                    emi_flow=emi_flow)
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    # print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        flag=DEFAULT_FLAG,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+ " Loan Amount",disposition_id="APTP",
                        ptp_date= given_date,
                        emi_flow=emi_flow)
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            flag=DEFAULT_FLAG,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+ " Loan Amount",disposition_id="UPTP",
                            ptp_date=given_date,
                            emi_flow=emi_flow)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]

class ActionClientName(Action):
    def name(self):
        return "action_client_name"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        principal_amount = tracker.get_slot("principal_amount_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        client_name = tracker.get_slot("client_name_slot")
        bank_name = tracker.get_slot("bank_name_slot")
        intent = tracker.latest_message.get("temp_intent").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        print("The value of client_name", client_name)
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        if bank_name != "":
            dispatcher.utter_template(
                "utter_action_by_bot_client_name_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker,
                principal_amount=principal_amount,
                client_name=bank_name,
            )
        else:
            dispatcher.utter_template(
                "utter_quantitative_data_alt_response_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Loan Information",
                    emi_flow=emi_flow)
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    # print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        flag=DEFAULT_FLAG,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Loan Information",disposition_id="APTP",
                        ptp_date= given_date,
                        emi_flow=emi_flow)
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            flag=DEFAULT_FLAG,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Loan Information",disposition_id="UPTP",
                            ptp_date=given_date,
                            emi_flow=emi_flow)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class ActionInterestRate(Action):
    def name(self):
        return "action_interest_rate"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        interest_rate = tracker.get_slot("interest_rate_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if signal == "interest_rate" and (sub_context == "quantitative_data" or sub_context == "action_by_bot") and interest_rate != "":
            dispatcher.utter_template(
                "utter_action_by_bot_intrest_rate_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker,
                intrest_rate=interest_rate,
                interest_rate =interest_rate)
        if interest_rate == "":
            dispatcher.utter_template(
                "utter_quantitative_data_alt_response_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Interest Rate",
                    emi_flow=emi_flow)
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        if len(entities)>0:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    # print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        flag=DEFAULT_FLAG,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Interest Rate",disposition_id="APTP",
                        ptp_date=given_date,
                        emi_flow=emi_flow)
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            flag=DEFAULT_FLAG,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Interest Rate",disposition_id="UPTP",
                            ptp_date=given_date,
                            emi_flow=emi_flow)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]
        if delay_reason_needed == "yes":
            if signal == "interest_rate" and delay_reason == "high_interest_rate":
                dispatcher.utter_template(
                    "utter_high_interest_rate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender,
                    tracker)
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - High Interest Rate",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionPropertyDispute(Action):
    def name(self):
        return "action_property_dispute"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        partial_payment = tracker.get_slot("partial_payment_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        sms_integration = tracker.get_slot("sms_integration_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        came_from_delay_reason = tracker.get_slot("came_from_delay_reason")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        variation = tracker.get_slot("variation_slot")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            if delay_reason == "property_dispute" and partial_payment == "no" or partial_payment_count == "triggered":
                dispatcher.utter_template(
                    "utter_property_dispute_"+variation+emi_flow+"_"
                    + region
                    + gender
                    + age_category
                    + collared
                    + "_"
                    + typology
                    + bot_gender,
                    tracker,
                )
            if came_from_delay_reason == "True" or  partial_payment_count == "triggered":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Property Dispute",
                    emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
            if partial_payment == "yes":
                send_and_store_disposition_details(
                tracker=tracker,
                flag=DEFAULT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Property Dispute",disposition_id="Minimum Amount Due Requested",
                emi_flow=emi_flow)
                return [FollowupAction("partial_payment_lvl1_form"), SlotSet(REQUESTED_SLOT,None),SlotSet("partial_payment_slot",str(partial_payment)),
                    SlotSet("level_of_negotiation_slot",str(level_of_negotiation)), SlotSet("changing_slot",str(REQUESTED_SLOT2)) ,
                    SlotSet("sms_integration_slot",str(sms_integration)),SlotSet("trail_count",None),SlotSet("came_from_delay_reason","True"),SlotSet("partial_payment_count","triggered")]
            else:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Property Dispute",
                    emi_flow=emi_flow)
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionPersoanlIssue(Action):
    def name(self):
        return "action_personal_issue"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        partial_payment = tracker.get_slot("partial_payment_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        sms_integration = tracker.get_slot("sms_integration_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        came_from_delay_reason = tracker.get_slot("came_from_delay_reason")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        variation = tracker.get_slot("variation_slot")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            if delay_reason == "personal_issue" and partial_payment == "no" or partial_payment_count == "triggered":
                dispatcher.utter_template(
                    "utter_personal_issue_"+variation+emi_flow+"_"
                    + region
                    + gender
                    + age_category
                    + collared
                    + "_"
                    + typology
                    + bot_gender,
                    tracker,
                )
            print("The valuye od partial payment ((((((",partial_payment)
            if came_from_delay_reason == "True" or  partial_payment_count == "triggered":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Personal Issue",
                    emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
            if partial_payment == "yes":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Personal Issue",disposition_id="Minimum Amount Due Requested",
                    emi_flow=emi_flow)
                return [FollowupAction("partial_payment_lvl1_form"), SlotSet(REQUESTED_SLOT,None), SlotSet("changing_slot",str(REQUESTED_SLOT2)) ,
                    SlotSet("trail_count",None),SlotSet("came_from_delay_reason","True"),SlotSet("partial_payment_count","triggered")]
            else:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Personal Issue",
                    emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionOutOfStation(Action):
    def name(self):
        return "action_out_of_station"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        variation = tracker.get_slot("variation_slot")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            print("The value os i am out of station", delay_reason)
            template = (
                "utter_out_of_station_"+variation+emi_flow+"_"
                + region
                + gender
                + age_category
                + collared
                + "_"
                + typology
                + bot_gender
            )
            print("The out template", template)
            dispatcher.utter_template(template, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Out Of Station",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionFamilyMatter(Action):
    def name(self):
        return "action_family_matter"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        partial_payment = tracker.get_slot("partial_payment_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        sms_integration = tracker.get_slot("sms_integration_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        came_from_delay_reason = tracker.get_slot("came_from_delay_reason")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            if delay_reason == "family_matter" and partial_payment == "no" or partial_payment_count == "triggered":
                dispatcher.utter_template(
                    "utter_family_matter_"+emi_flow+"_static" + SRP + bot_gender, tracker
                )
            if came_from_delay_reason == "True" or  partial_payment_count == "triggered":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Family Matter",
                    emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
            if partial_payment == "yes":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Family Matter",disposition_id="Minimum Amount Due Requested",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("partial_payment_lvl1_form"), SlotSet(REQUESTED_SLOT,None), SlotSet("changing_slot",str(REQUESTED_SLOT2)) ,
                    SlotSet("trail_count",None),SlotSet("came_from_delay_reason","True"),SlotSet("partial_payment_count","triggered")]
            else:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Family Matter",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionBusinessLoss(Action):
    def name(self):
        return "action_business_loss"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        partial_payment = tracker.get_slot("partial_payment_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        sms_integration = tracker.get_slot("sms_integration_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        came_from_delay_reason = tracker.get_slot("came_from_delay_reason")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            if delay_reason == "business_loss" and partial_payment == "no" or partial_payment_count == "triggered":
                dispatcher.utter_template(
                    "utter_business_loss_"+emi_flow+"_static" + SRP + bot_gender, tracker
                )
            if came_from_delay_reason == "True" or  partial_payment_count == "triggered":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Business Loss",
                    emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
            if partial_payment == "yes":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Business Loss",disposition_id="Minimum Amount Due Requested",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("partial_payment_lvl1_form"), SlotSet(REQUESTED_SLOT,None), SlotSet("changing_slot",str(REQUESTED_SLOT2)) ,
                    SlotSet("trail_count",None),SlotSet("came_from_delay_reason","True"),SlotSet("partial_payment_count","triggered")]
            else:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Business Loss",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionBusinessClosed(Action):
    def name(self):
        return "action_business_closed"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        partial_payment = tracker.get_slot("partial_payment_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        sms_integration = tracker.get_slot("sms_integration_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        partial_payment_count = tracker.get_slot("partial_payment_count")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            if delay_reason == "business_closed":
                if partial_payment == "yes" and partial_payment_count == "not_triggered":
                    send_and_store_disposition_details(
                        tracker=tracker,
                        flag=DEFAULT_FLAG,
                        dispatcher=dispatcher,
                        disposition_details="Delay - Business Closed",disposition_id="Minimum Amount Due Requested",
                        emi_flow=emi_flow,
                    )
                    return [FollowupAction("partial_payment_lvl1_form"), SlotSet(REQUESTED_SLOT,None), SlotSet("changing_slot",str(REQUESTED_SLOT2)) ,
                        SlotSet("trail_count",None),SlotSet("came_from_delay_reason","True"),SlotSet("partial_payment_count","triggered")]
                else:
                    template_name = "utter_business_closed_"+emi_flow+"_static" + SRP + bot_gender
                    dispatcher.utter_template(template_name, tracker)
                    send_and_store_disposition_details(
                        tracker=tracker,
                        flag=TIMEOUT_FLAG,
                        dispatcher=dispatcher,
                        disposition_details="Delay - Business Closed",
                        emi_flow=emi_flow,
                    )
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionChequeBonce(Action):
    def name(self):
        return "action_cheque_bounce"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            dispatcher.utter_template(
                "utter_cheque_bounce_"+emi_flow+"_static" + SRP + bot_gender, tracker
            )
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Cheque Bounce",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]

class ActionUnprofessionalEmployee(Action):
    def name(self):
        return "action_unprofessional_employee"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        # if delay_reason_needed == "yes":
        dispatcher.utter_template(
            "utter_unprofessional_employee_"+emi_flow+"_static" + SRP + bot_gender,
            tracker,
        )
        send_and_store_disposition_details(
            tracker=tracker,
            flag=TIMEOUT_FLAG,
            dispatcher=dispatcher,
            disposition_details="General - Unprofessional Employee",
            disposition_id = "Dispute",
            emi_flow=emi_flow,
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]
        # else:
        #     return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]

class ActionFraudSale(Action):
    def name(self):
        return "action_fraud_sale"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        # if delay_reason_needed == "yes":
        dispatcher.utter_template(
            "utter_fraud_sale_"+emi_flow+"_static" + SRP + bot_gender, tracker
        )
        send_and_store_disposition_details(
            tracker=tracker,
            flag=TIMEOUT_FLAG,
            dispatcher=dispatcher,
            disposition_details="General - Fraud Sales",
            disposition_id = "Dispute",
            emi_flow=emi_flow,
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]
        # else:
        #     # return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]
        #     #for nly paytm
        #     dispatcher.utter_template(
        #         "utter_fraud_sale_"+emi_flow+"_static" + SRP + bot_gender, tracker
        #     )
        #     send_and_store_disposition_details(
        #         tracker=tracker,
        #         flag=TIMEOUT_FLAG,
        #         dispatcher=dispatcher,
        #         disposition_details="Delay - Fraud Sales",
        #         emi_flow=emi_flow,
        #     )
        #     return [FollowupAction("action_listen"), AllSlotsReset()]
    

class ActionHighInterestRate(Action):
    def name(self):
        return "action_high_interest_rate"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        signal = tracker.latest_message.get("signal").get("name")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        # if delay_reason_needed == "yes":
        # if signal == "high_interest_rate":
        dispatcher.utter_template(
            "utter_high_interest_rate_"+emi_flow+"_static" + SRP + bot_gender, tracker
        )
        send_and_store_disposition_details(
            tracker=tracker,
            flag=TIMEOUT_FLAG,
            dispatcher=dispatcher,
            disposition_details="Delay - High interest rate",
            disposition_id = "Dispute",
            emi_flow=emi_flow,
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]
        # else:
        #     send_and_store_disposition_details(tracker=tracker,
        #                         dispatcher=dispatcher,flag=DEFAULT_FLAG)
        #     return get_return_values(tracker)
        # else:
        #     return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionEmiDateNotInformed(Action):
    def name(self):
        return "action_emi_date_not_informed"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        variation = tracker.get_slot("variation_slot")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            dispatcher.utter_template(
                "utter_emi_date_not_confirmed_"+variation+emi_flow+"_"
                + region
                + gender
                + age_category
                + collared
                + "_"
                + typology
                + bot_gender,
                tracker,
            )
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Date Not Informed",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionSalaryNotRecevied(Action):
    def name(self):
        return "action_salary_not_received"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        partial_payment = tracker.get_slot("partial_payment_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        sms_integration = tracker.get_slot("sms_integration_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        came_from_delay_reason = tracker.get_slot("came_from_delay_reason")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            if partial_payment == "no" or partial_payment_count == "triggered":
                template_name = "utter_salary_not_received_"+emi_flow+"_static" + SRP + bot_gender
                print("The generated template name", template_name)
                dispatcher.utter_template(template_name, tracker)  
            if came_from_delay_reason == "True" or partial_payment_count == "triggered":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Salary Issues",
                    emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
        
            if partial_payment == "yes":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Salary Issues",disposition_id="Minimum Amount Due Requested",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("partial_payment_lvl1_form"), SlotSet(REQUESTED_SLOT,None), SlotSet("changing_slot",str(REQUESTED_SLOT2)) ,
                    SlotSet("trail_count",None),SlotSet("came_from_delay_reason","True"),SlotSet("partial_payment_count","triggered")]
            else:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Salary Issues",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionSalaryTimeSpecificDelay(Action):
    def name(self):
        return "action_salary_time_specific_delay"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        partial_payment = tracker.get_slot("partial_payment_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        sms_integration = tracker.get_slot("sms_integration_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        came_from_delay_reason = tracker.get_slot("came_from_delay_reason")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            if delay_reason == "salary_time_specific_delay" and partial_payment == "no" or partial_payment_count == "triggered":
                template_name = (
                    "utter_salary_time_specific_delay_"+emi_flow+"_static" + SRP + bot_gender
                )
                print("The generated template name", template_name)
                dispatcher.utter_template(template_name, tracker)
            if came_from_delay_reason == "True" and partial_payment_count == "not_triggered":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Salary Time Delayed",emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
            if partial_payment == "yes":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Salary Time Delayed",disposition_id="Minimum Amount Due Requested",
                    emi_flow=emi_flow)
                return [FollowupAction("partial_payment_lvl1_form"), SlotSet(REQUESTED_SLOT,None), SlotSet("changing_slot",str(REQUESTED_SLOT2)) ,
                    SlotSet("trail_count",None),SlotSet("came_from_delay_reason","True"),SlotSet("partial_payment_count","triggered")]
            else:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Salary Time Delayed",
                    emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionJobless(Action):
    def name(self):
        return "action_jobless"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        partial_payment = tracker.get_slot("partial_payment_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        sms_integration = tracker.get_slot("sms_integration_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        came_from_delay_reason = tracker.get_slot("came_from_delay_reason")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        variation = tracker.get_slot("variation_slot")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            if delay_reason == "jobless" and partial_payment == "no" or partial_payment_count == "triggered":
                template_name = (
                    "utter_jobless_"+variation+emi_flow+"_"
                    + region
                    + gender
                    + age_category
                    + collared
                    + "_"
                    + typology
                    + bot_gender
                )
                print("The generated template name", template_name)
                dispatcher.utter_template(template_name, tracker)
            if came_from_delay_reason == "True" or  partial_payment_count == "triggered":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Jobless",
                    emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
            if partial_payment == "yes":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Jobless",disposition_id="Minimum Amount Due Requested",
                    emi_flow=emi_flow)
                return [FollowupAction("partial_payment_lvl1_form"), SlotSet(REQUESTED_SLOT,None), SlotSet("changing_slot",str(REQUESTED_SLOT2)) ,
                    SlotSet("trail_count",None),SlotSet("came_from_delay_reason","True"),SlotSet("partial_payment_count","triggered")]
            else:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Jobless",
                    emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionJobLoss(Action):
    def name(self):
        return "action_job_loss"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        partial_payment = tracker.get_slot("partial_payment_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        sms_integration = tracker.get_slot("sms_integration_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        came_from_delay_reason = tracker.get_slot("came_from_delay_reason")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        variation = tracker.get_slot("variation_slot")
        print("cam from dely reaon",came_from_delay_reason)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            if delay_reason == "job loss" and partial_payment == "no" or partial_payment_count == "triggered":
                template_name = (
                    "utter_job_loss_"+variation+emi_flow+"_"
                    + region
                    + gender
                    + age_category
                    + collared
                    + "_"
                    + typology
                    + bot_gender
                )
                print("The generated template name", template_name)
                dispatcher.utter_template(template_name, tracker)
            if came_from_delay_reason == "True" or  partial_payment_count == "triggered":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Jobloss",
                    emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
            if partial_payment == "yes":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Jobloss",disposition_id="Minimum Amount Due Requested",
                    emi_flow=emi_flow)
                return [FollowupAction("partial_payment_lvl1_form"), SlotSet(REQUESTED_SLOT,None), SlotSet("changing_slot",str(REQUESTED_SLOT2)) ,
                    SlotSet("trail_count",None),SlotSet("came_from_delay_reason","True"),SlotSet("partial_payment_count","triggered")]
            else:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Jobloss",
                    emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionCustomerDeath(Action):
    def name(self):
        return "action_customer_death"
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        account_name = tracker.get_slot("account_name_slot")
        insurance =  tracker.get_slot("insurance_slot")
        print("cskcsd",insurance)
        # if (account_name == "Bajaj Finserv Counselling Flow Testing" or account_name == "Bajaj Finserv Counselling Flow"):
        #     template_name = (
        #         "utter_customer_death_"+emi_flow+"_static"
        #         +SRP
        #         + bot_gender
        #     )
        #     print("The generated template name", template_name)
        #     dispatcher.utter_template(template_name, tracker)
        #     send_and_store_disposition_details(
        #         tracker=tracker,
        #         flag=TIMEOUT_FLAG,
        #         dispatcher=dispatcher,
        #         disposition_details="Delay - User Death",
        #         emi_flow=emi_flow,
        #     )
        if (delay_reason_needed == "yes" and insurance == "yes"):
            return [FollowupAction("customer_death_form"),SlotSet("trail_count", 1), SlotSet(REQUESTED_SLOT,None)]
        if (delay_reason_needed == "yes" or account_name == "PayTM Testing" or account_name == "PayTM"):
            template_name = (
                "utter_customer_death_"+emi_flow+"_static"
                +SRP
                + bot_gender
            )
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - User Death",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionUnableToFindWork(Action):
    def name(self):
        return "action_unable_to_find_work"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        partial_payment = tracker.get_slot("partial_payment_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        sms_integration = tracker.get_slot("sms_integration_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        came_from_delay_reason = tracker.get_slot("came_from_delay_reason")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        variation = tracker.get_slot("variation_slot")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            if delay_reason == "unable_to_find_work" and partial_payment == "no" or partial_payment_count == "triggered":
                template_name = (
                    "utter_unable_to_find_work_"+variation+emi_flow+"_"
                    + region
                    + gender
                    + age_category
                    + collared
                    + "_"
                    + typology
                    + bot_gender
                )
                print("The generated template name", template_name)
                dispatcher.utter_template(template_name, tracker)
            if came_from_delay_reason == "True" or  partial_payment_count == "triggered":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Unable To Find Job",emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
            if partial_payment == "yes":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Unable To Find Job",disposition_id="Minimum Amount Due Requested",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("partial_payment_lvl1_form"), SlotSet(REQUESTED_SLOT,None), SlotSet("changing_slot",str(REQUESTED_SLOT2)) ,
                    SlotSet("trail_count",None),SlotSet("came_from_delay_reason","True"),SlotSet("partial_payment_count","triggered")]
            else:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Unable To Find Job",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionForgotDueDate(Action):
    def name(self):
        return "action_forgot_due_date"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        due_date= tracker.get_slot("due_date")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = "utter_forgot_due_date_"+emi_flow+"_static" + SRP + bot_gender
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker,monthly_emi_date=due_date )
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Forgot Due Date",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionBranchIssue(Action):
    def name(self):
        return "action_branch_issue"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        payment_method = paymentMode(tracker,"available_payment_mode")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = "utter_branch_issue_"+emi_flow+"_static" + SRP + bot_gender
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker,available_payment_mode=payment_method)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Branch Issue",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionForgotPayment(Action):
    def name(self):
        return "action_forgot_payment"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        print("coming3685")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = "utter_forgot_payment_"+emi_flow+"_static" + SRP + bot_gender
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Forgot Payment",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionAccountNotActiveOrAvailable(Action):
    def name(self):
        return "action_account_not_active_or_available"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = (
                "utter_account_not_active_or_available_"+emi_flow+"_static" + SRP + bot_gender
            )
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Account Inactive",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionUserHealthIssue(Action):
    def name(self):
        return "action_user_health_issue"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            if delay_reason == "user_health_issue" or delay_reason == "general_medical_emergency":
                template_name = (
                    "utter_customer_health_issue_"+emi_flow+"_static" + SRP + bot_gender
                )
                print("The generated template name", template_name)
                dispatcher.utter_template(template_name, tracker)
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - User Health Issue",
                    emi_flow=emi_flow,
                )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionFamilyHealthIssue(Action):
    def name(self):
        return "action_family_health_issue"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = "utter_family_health_issue_"+emi_flow+"_static" + SRP + bot_gender
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Family Health Issue",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionUserDeath(Action):
    def name(self):
        return "action_user_death"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = "utter_customer_death_"+emi_flow+"_static" + SRP + bot_gender
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - User Death",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]

class ActionDeathInFamily(Action):
    def name(self):
        return "action_death_in_family"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = "utter_death_in_family_"+emi_flow+"_static" + SRP + bot_gender
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Death In Family",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionClientOrApplicationIssue(Action):
    def name(self):
        return "action_client_or_application_issue"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            if delay_reason == ("client_issue" or "application_issue"):
                template_name = (
                    "utter_client_or_application_issue_"+emi_flow+"_static" + SRP + bot_gender
                )
                print("The generated template name", template_name)
                dispatcher.utter_template(template_name, tracker)
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Application Issue",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionPaymentGatewayIssue(Action):
    def name(self):
        return "action_payment_gateway_issue"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = (
                "utter_payment_gateway_issue_"+emi_flow+"_static" + SRP + bot_gender
            )
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Payment Gateway Issue",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]

class ActionUserTechnicalIssue(Action):
    def name(self):
        return "action_user_technical_issue"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        signal = tracker.latest_message.get("signal").get("name")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if signal == "telephone_network_issue":
            dispatcher.utter_template(
                "utter_network_problem_"+emi_flow+"_static" + SRP + bot_gender, tracker
            )
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="General - Network Issue",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        if delay_reason_needed == "yes":
            template_name = (
                "utter_customer_technical_issue_"+emi_flow+"_static" + SRP + bot_gender
            )
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Technical Issue",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionAccountGettingUpdated(Action):
    def name(self):
        return "action_account_getting_updated"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = (
                "utter_account_getting_updated_"+emi_flow+"_static" + SRP + bot_gender
            )
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Account Updating",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionAccountClosed(Action):
    def name(self):
        return "action_account_closed"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = "utter_account_closed_"+emi_flow+"_static" + SRP + bot_gender
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Account Closed",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            # return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]
            #only for paytm
            template_name = "utter_account_closed_"+emi_flow+"_static" + SRP + bot_gender
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Account Closed",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
class ActionInsufficientFunds(Action):
    def name(self):
        return "action_insufficient_funds"
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        partial_payment = tracker.get_slot("partial_payment_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        sms_integration = tracker.get_slot("sms_integration_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        came_from_delay_reason = tracker.get_slot("came_from_delay_reason")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            if delay_reason == "insufficient_funds" and partial_payment == "no" or partial_payment_count == "triggered":
                template_name = (
                            "utter_insufficient_funds_"+emi_flow+"_static"
                            +SRP
                            + bot_gender
                        )
                print("The generated template name", template_name)
                dispatcher.utter_template(template_name, tracker)
            if came_from_delay_reason == "True" or  partial_payment_count == "triggered":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Insufficient Funds",
                    emi_flow=emi_flow)
                return [FollowupAction("action_listen"), AllSlotsReset()]
            if partial_payment == "yes":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Insufficient Funds",disposition_id="Minimum Amount Due Requested",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("partial_payment_lvl1_form"), SlotSet(REQUESTED_SLOT,None), SlotSet("changing_slot",str(REQUESTED_SLOT2)) ,
                    SlotSet("trail_count",None),SlotSet("came_from_delay_reason","True"),SlotSet("partial_payment_count","triggered")]
            else:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Insufficient Funds",
                    emi_flow=emi_flow,
                )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]



class ActionAccountTransactionLimitCompleted(Action):
    def name(self):
        return "action_account_transaction_limit_completed"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        variation = tracker.get_slot("variation_slot")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = (
                "utter_account_transaction_limit_completed_"+variation+emi_flow+"_"
                + region
                + gender
                + age_category
                + collared
                + "_"
                + typology
                + bot_gender
            )
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
            tracker=tracker,
            flag=TIMEOUT_FLAG,
            dispatcher=dispatcher,
            disposition_details="Delay - Transaction Limit Exceeded",
            emi_flow=emi_flow)
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionAccountGeneralIssue(Action):
    def name(self):
        return "action_account_general_issue"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = (
                "utter_account_general_issue_"+emi_flow+"_static" + SRP + bot_gender
            )
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Account Issue",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            template_name = (
                "utter_account_general_issue_"+emi_flow+"_static" + SRP + bot_gender
            )
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Account Issue",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
            #only for paytm
            # return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionNotHandledDelayReason(Action):
    def name(self):
        return "action_not_handled_delay_reason"

    def run(self, dispatcher, tracker, domain):
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = (
                "utter_not_handled_delay_reason_"+emi_flow+"_static" + SRP + bot_gender
            )
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Others",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]

class ActionPayBranch(Action):
    def name(self):
        return "action_pay_via_branch"

    def run(self, dispatcher, tracker, domain):
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        entities = tracker.latest_message["entities"]
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        eligible = tracker.get_slot("pay_via_branch_slot")
        payment_method = paymentMode(tracker,"available_payment_mode")
        threshold_days = tracker.get_slot("threshold_days_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        temp_intent =tracker.latest_message.get("temp_intent").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        print("The value of eligible", eligible)
        account_name = tracker.get_slot("account_name_slot")
        if eligible == "yes":
            if (account_name == "Aadhar Housing Finance" or account_name == "Aadhar Housing Finance Testing") and ("dpd" in emi_flow):
                return [FollowupAction("pay_via_cash_form"),SlotSet("trail_count", 1), SlotSet(REQUESTED_SLOT,None)]
            if temp_intent == "ask" and sub_context == "process":
                print("enterint into ask or inform intent with preocess")
                template_name = (
                    "utter_process_pay_via_branch_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker, user_requested_payment_option="branch",online_payment_option = "branch",available_payment_mode=payment_method)
            elif temp_intent == "inform" and context == "payment" and sub_context == "action_by_customer" and sub_intent == "affirm" and emi_flow!="predue":
                if len(entities) == 0:
                    todays_date = datetime.date.today().strftime("%d %B %Y").lstrip('0')
                    dispatcher.utter_template(
                                "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker)
                    print("Entering into AccPTP Affirm")
                    send_and_store_disposition_details(
                                tracker=tracker,
                                dispatcher=dispatcher,
                                disposition_details=temp_intent.capitalize()+" Branch Payment",disposition_id="APTP",
                                ptp_date= todays_date,
                                flag=TIMEOUT_FLAG,
                            )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
            elif temp_intent == "ask" or temp_intent == "inform":
                print("enterint into ask or inform intent")
                template_name = (
                    "utter_action_by_customer_payment_option_available_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker, user_requested_payment_mode="branch",user_requested_payment_option="branch",online_payment_option = "branch",available_payment_mode=payment_method)
        else:
            if auto_debit=="auto debit":
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+auto_debit_nach+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            else:
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            dispatcher.utter_template(
                template,
                tracker,
                user_requested_payment_option="branch",
                available_payment_mode=payment_method,
            )
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    disposition_details=temp_intent.capitalize()+" Branch Payment",
                    flag=DEFAULT_FLAG,
                )
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    dispatcher.utter_template(
                        "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    )
                    print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" Branch Payment",disposition_id="APTP",
                        ptp_date= given_date,
                        flag=TIMEOUT_FLAG,
                    )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=temp_intent.capitalize()+" Branch Payment",disposition_id="UPTP",
                            ptp_date= given_date,
                            flag=DEFAULT_FLAG,
                        )
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class PayViaNetBanking(Action):
    def name(self):
        return "action_pay_via_net_banking"

    def run(self, dispatcher, tracker, domain):
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        entities = tracker.latest_message["entities"]
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        eligible = tracker.get_slot("pay_via_net_banking_slot")
        payment_method = paymentMode(tracker,"available_payment_mode")
        threshold_days = tracker.get_slot("threshold_days_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        temp_intent = tracker.latest_message.get("temp_intent").get("name")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        print("The value of eligible", eligible)
        if eligible == "yes":
            if temp_intent == "ask" and sub_context == "process":
                print("enterint into ask or inform intent with preocess")
                template_name = (
                    "utter_process_pay_via_netbanking_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker, user_requested_payment_option="net banking",online_payment_option = "net banking",available_payment_mode=payment_method)
            elif temp_intent == "inform" and context == "payment" and sub_context == "action_by_customer" and sub_intent == "affirm" and emi_flow!="predue":
                if len(entities) == 0:
                    todays_date = datetime.date.today().strftime("%d %B %Y").lstrip('0')
                    dispatcher.utter_template(
                                "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker)
                    print("Entering into AccPTP Affirm")
                    send_and_store_disposition_details(
                                tracker=tracker,
                                dispatcher=dispatcher,
                                disposition_details=temp_intent.capitalize()+" Netbanking",disposition_id="APTP",
                                ptp_date= todays_date,
                                flag=TIMEOUT_FLAG,
                            )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
            elif temp_intent == "ask" or temp_intent == "inform":
                print("enterint into ask or inform intent")
                template_name = (
                    "utter_action_by_customer_payment_option_available_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker,user_requested_payment_mode="net banking", user_requested_payment_option="net banking",online_payment_option = "net banking",available_payment_mode=payment_method)
        else:
            if auto_debit=="auto debit":
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+auto_debit_nach+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            else:
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            dispatcher.utter_template(
                template,
                tracker,
                user_requested_payment_option="netbanking",
                available_payment_mode=payment_method,
            )
        if len(entities) == 0:
            print("Entering into NoPTP")
            send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=temp_intent.capitalize()+" Netbanking", #disp
                            flag=TIMEOUT_FLAG,
            )
            if tracker.active_form.get("name") is not None:
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    dispatcher.utter_template(
                        "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    )
                    print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" Netbanking",disposition_id="APTP", #disp
                        ptp_date=given_date,
                        flag=TIMEOUT_FLAG,
                    )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=temp_intent.capitalize()+" Netbanking",disposition_id="UPTP",
                            ptp_date=given_date,
                            flag=DEFAULT_FLAG,
                        )
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class PayViaNetAgent(Action):
    def name(self):
        return "action_pay_via_agent"

    def run(self, dispatcher, tracker, domain):
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        entities = tracker.latest_message["entities"]
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        eligible = tracker.get_slot("pay_via_agent_slot")
        payment_method = paymentMode(tracker,"available_payment_mode")
        threshold_days = tracker.get_slot("threshold_days_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        temp_intent = tracker.latest_message.get("temp_intent").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        print("The value of eligible", eligible)
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        account_name = tracker.get_slot("account_name_slot")
        if eligible == "yes":
            print("cdjow")
            if (account_name == "Aadhar Housing Finance" or account_name == "Aadhar Housing Finance Testing") and ("dpd" in emi_flow):
                print("cdjow1234")
                return [FollowupAction("pay_via_cash_form"),SlotSet("trail_count", 1), SlotSet(REQUESTED_SLOT,None)]
            if temp_intent == "ask" and sub_context == "process":
                print("enterint into ask or inform intent with preocess")
                template_name = (
                    "utter_process_pay_via_agent_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker, user_requested_payment_option="agent",online_payment_option = "agent",available_payment_mode=payment_method)
            elif temp_intent == "inform" and context == "payment" and sub_context == "action_by_customer" and sub_intent == "affirm" and emi_flow!="predue":
                if len(entities) == 0:
                    todays_date = datetime.date.today().strftime("%d %B %Y").lstrip('0')
                    dispatcher.utter_template(
                                "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker)
                    print("Entering into AccPTP Affirm")
                    send_and_store_disposition_details(
                                tracker=tracker,
                                dispatcher=dispatcher,
                                disposition_details=temp_intent.capitalize()+" Agent Payment",disposition_id="APTP",
                                ptp_date= todays_date,
                                flag=TIMEOUT_FLAG,
                            )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
            elif temp_intent == "ask" or temp_intent == "inform":
                print("enterint into ask or inform intent")
                template_name = (
                    "utter_action_by_customer_payment_option_available_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker,user_requested_payment_mode="agent", user_requested_payment_option="agent",online_payment_option = "agent",available_payment_mode=payment_method)
        else:
            if auto_debit=="auto debit":
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+auto_debit_nach+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            else:
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            dispatcher.utter_template(
                template,
                tracker,
                user_requested_payment_option="agent",
                available_payment_mode=payment_method,
            )
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" Agent Payment",
                        flag=DEFAULT_FLAG,
                    )
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    dispatcher.utter_template(
                        "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    )
                    print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" Agent Payment",disposition_id="APTP",
                        ptp_date= given_date,
                        flag=TIMEOUT_FLAG,
                    )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")

                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=temp_intent.capitalize()+" Agent Payment",disposition_id="UPTP",
                            ptp_date= given_date,
                            flag=DEFAULT_FLAG,)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class PayViaApp(Action):
    def name(self):
        return "action_pay_via_app"

    def run(self, dispatcher, tracker, domain):
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        entities = tracker.latest_message["entities"]
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        eligible = tracker.get_slot("pay_via_app_slot")
        payment_method = paymentMode(tracker,"available_payment_mode")
        threshold_days = tracker.get_slot("threshold_days_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        temp_intent = tracker.latest_message.get("temp_intent").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        print("The value of eligible", eligible)
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason == "application_issue":
            if delay_reason_needed == "yes":
                template_name = (
                "utter_client_or_application_issue_"+emi_flow+"_static" + SRP + bot_gender)
                print("The generated template name", template_name)
                dispatcher.utter_template(template_name, tracker)
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Application Issue",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
            else:
                return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]
        if eligible == "yes":
            if temp_intent == "ask" and sub_context == "process":
                print("enterint into ask or inform intent with preocess")
                template_name = (
                    "utter_process_pay_via_app_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker, user_requested_payment_option="app",online_payment_option = "app",available_payment_mode=payment_method)
            elif temp_intent == "inform" and context == "payment" and sub_context == "action_by_customer" and sub_intent == "affirm" and emi_flow!="predue":
                if len(entities) == 0:
                    todays_date = datetime.date.today().strftime("%d %B %Y").lstrip('0')
                    dispatcher.utter_template(
                                "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker)
                    print("Entering into AccPTP Affirm")
                    send_and_store_disposition_details(
                                tracker=tracker,
                                dispatcher=dispatcher,
                                disposition_details=temp_intent.capitalize()+" App Payment",disposition_id="APTP",
                                ptp_date= todays_date,
                                flag=TIMEOUT_FLAG,
                            )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
            elif temp_intent == "ask" or temp_intent == "inform":
                print("enterint into ask or inform intent")
                template_name = (
                    "utter_action_by_customer_payment_option_available_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker, user_requested_payment_mode="app",user_requested_payment_option="app",online_payment_option = "app",available_payment_mode=payment_method)
        else:
            if auto_debit=="auto debit":
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+auto_debit_nach+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            else:
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            dispatcher.utter_template(
                template,
                tracker,
                user_requested_payment_option="app",
                available_payment_mode=payment_method,
            )
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" App Payment",
                        flag=DEFAULT_FLAG,
                    )
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:  
                    dispatcher.utter_template(
                        "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    )
                    print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" App Payment",disposition_id="APTP",
                        ptp_date= given_date,
                        flag=TIMEOUT_FLAG,
                    )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
                else:
                    print("Entering into Not AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" App Payment",disposition_id="UPTP",
                        ptp_date= given_date,
                        flag=DEFAULT_FLAG,
                    )
                    return decide_slot(tracker)


class PayViaCard(Action):
    def name(self):
        return "action_pay_via_card"

    def run(self, dispatcher, tracker, domain):
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        entities = tracker.latest_message["entities"]
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        eligible = tracker.get_slot("pay_via_card_slot")
        payment_method = paymentMode(tracker,"available_payment_mode")
        threshold_days = tracker.get_slot("threshold_days_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        temp_intent = tracker.latest_message.get("temp_intent").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        print("The value of eligible", eligible)
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        if eligible == "yes":
            if temp_intent == "ask" and sub_context == "process":
                print("enterint into ask or inform intent with preocess")
                template_name = (
                    "utter_process_pay_via_card_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker, user_requested_payment_option="card",online_payment_option = "card",available_payment_mode=payment_method)
            elif temp_intent == "inform" and context == "payment" and sub_context == "action_by_customer" and sub_intent == "affirm" and emi_flow!="predue":
                if len(entities) == 0:
                    todays_date = datetime.date.today().strftime("%d %B %Y").lstrip('0')
                    dispatcher.utter_template(
                                "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker)
                    print("Entering into AccPTP Affirm")
                    send_and_store_disposition_details(
                                tracker=tracker,
                                dispatcher=dispatcher,
                                disposition_details=temp_intent.capitalize()+" Card Payment",disposition_id="APTP",
                                ptp_date= todays_date,
                                flag=TIMEOUT_FLAG,
                            )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
            elif temp_intent == "ask" or temp_intent == "inform":
                print("enterint into ask or inform intent")
                template_name = (
                    "utter_action_by_customer_payment_option_available_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker, user_requested_payment_mode="card",user_requested_payment_option="card",online_payment_option = "card",available_payment_mode=payment_method)
        else:
            if auto_debit=="auto debit":
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+auto_debit_nach+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            else:
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            dispatcher.utter_template(
                template,
                tracker,
                user_requested_payment_option="card",
                available_payment_mode=payment_method,
            )
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" Card Payment",
                        flag=DEFAULT_FLAG,
                    )
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    dispatcher.utter_template(
                        "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    )
                    print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" Card Payment",disposition_id="APTP",
                        ptp_date= given_date,
                        flag=TIMEOUT_FLAG,
                    )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
                else:
                    if tracker.active_form.get("name") is not None:
                        send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" Card Payment",disposition_id="UPTP",
                        ptp_date= given_date,
                        flag=DEFAULT_FLAG,)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class PayViaWallet(Action):
    def name(self):
        return "action_pay_via_wallet"

    def run(self, dispatcher, tracker, domain):
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        entities = tracker.latest_message["entities"]
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        eligible = tracker.get_slot("pay_via_wallet_slot")
        payment_method = paymentMode(tracker,"available_payment_mode")
        threshold_days = tracker.get_slot("threshold_days_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        temp_intent = tracker.latest_message.get("temp_intent").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        print("The value of eligible", eligible)
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        if eligible == "yes":
            if temp_intent == "ask" and sub_context == "process":
                print("enterint into ask or inform intent with preocess")
                template_name = (
                    "utter_process_pay_via_wallet_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker, user_requested_payment_option="wallet",online_payment_option = "wallet",available_payment_mode=payment_method)
            elif temp_intent == "inform" and context == "payment" and sub_context == "action_by_customer" and sub_intent == "affirm" and emi_flow!="predue":
                if len(entities) == 0:
                    todays_date = datetime.date.today().strftime("%d %B %Y").lstrip('0')
                    dispatcher.utter_template(
                                "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker)
                    print("Entering into AccPTP Affirm")
                    send_and_store_disposition_details(
                                tracker=tracker,
                                dispatcher=dispatcher,
                                disposition_details=temp_intent.capitalize()+" Wallet Payment",disposition_id="APTP",
                                ptp_date= todays_date,
                                flag=TIMEOUT_FLAG,
                            )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
            elif temp_intent == "ask" or temp_intent == "inform":
                print("enterint into ask or inform intent")
                template_name = (
                    "utter_action_by_customer_payment_option_available_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker, user_requested_payment_mode="wallet",user_requested_payment_option="wallet",online_payment_option = "wallet",available_payment_mode=payment_method)
        else:
            if auto_debit=="auto debit":
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+auto_debit_nach+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            else:
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            dispatcher.utter_template(
                template,
                tracker,
                user_requested_payment_option="wallet",
                available_payment_mode=payment_method,
            )
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=temp_intent.capitalize()+" Wallet Payment",
                            flag=DEFAULT_FLAG,
                        )
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    dispatcher.utter_template(
                        "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    )
                    print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" Wallet Payment",disposition_id="APTP",
                        ptp_date= given_date,
                        flag=TIMEOUT_FLAG,
                    )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")

                        send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" Wallet Payment",disposition_id="UPTP",
                        ptp_date= given_date,
                        flag=DEFAULT_FLAG)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class PayViaOnline(Action):
    def name(self):
        return "action_pay_via_online"

    def run(self, dispatcher, tracker, domain):
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        entities = tracker.latest_message["entities"]
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        eligible = tracker.get_slot("pay_via_online_slot")
        payment_method = paymentMode(tracker,"available_payment_mode")
        threshold_days = tracker.get_slot("threshold_days_slot")
        pay_online = tracker.get_slot("pay_online_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        move_to_new_slot = tracker.get_slot("move_to_new_slot")
        temp_intent = tracker.latest_message.get("temp_intent").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        print("The value of eligible", eligible)
        print("The value of intent",temp_intent)
        print("The value id sub cinre",sub_context)
        if eligible == "yes":
            if temp_intent == "ask" and sub_context == "process":
                print("enterint into ask or inform intent with preocess")
                template_name = (
                    "utter_process_pay_via_online_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker, user_requested_payment_option="online",online_payment_option = "online",available_payment_mode=payment_method)
            elif temp_intent == "inform" and context == "payment" and sub_context == "action_by_customer" and sub_intent == "affirm" and emi_flow!="predue":
                if len(entities) == 0:
                    todays_date = datetime.date.today().strftime("%d %B %Y").lstrip('0')
                    dispatcher.utter_template(
                                "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker)
                    print("Entering into AccPTP Affirm")
                    send_and_store_disposition_details(
                                tracker=tracker,
                                dispatcher=dispatcher,
                                disposition_details=temp_intent.capitalize()+" Online Payment",disposition_id="APTP",
                                ptp_date= todays_date,
                                flag=TIMEOUT_FLAG,
                            )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
            elif temp_intent == "ask" or temp_intent == "inform":
                print("enterint into ask or inform intent")
                template_name = (
                    "utter_action_by_customer_payment_option_available_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker, user_requested_payment_mode="online",user_requested_payment_option="online",online_payment_option = "online",available_payment_mode=payment_method)
        else:
            if auto_debit=="auto debit":
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+auto_debit_nach+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            else:
                template = (
                "utter_process_payment_option_not_available_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender
                )
            dispatcher.utter_template(
                template,
                tracker,
                user_requested_payment_option="online",
                available_payment_mode=payment_method,
            )
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    disposition_details=temp_intent.capitalize()+" Online Payment",
                    flag=DEFAULT_FLAG,
                )
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    dispatcher.utter_template(
                        "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    )
                    print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" Online Payment",disposition_id="APTP",
                        ptp_date= given_date,
                        flag=TIMEOUT_FLAG,
                    )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=temp_intent.capitalize()+" Online Payment",disposition_id="UPTP",
                            ptp_date= given_date,
                            flag=DEFAULT_FLAG,)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]


class ActionPayViaUPI(Action):
    def name(self):
        return "action_pay_via_upi"

    def run(self, dispatcher, tracker, domain):
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        entities = tracker.latest_message["entities"]
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        eligible = tracker.get_slot("pay_via_upi_slot")
        payment_method = paymentMode(tracker,"available_payment_mode")
        threshold_days = tracker.get_slot("threshold_days_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        temp_intent = tracker.latest_message.get("temp_intent").get("name")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        customer_language = tracker.get_slot("customer_language_slot")
        print("The valye of eligible", eligible)
        if customer_language == "english" or customer_language == "en":
            UPI = "UPI"
        elif customer_language == "hindi" or customer_language == "hi":
            UPI = "यूपीआई"
        elif customer_language == "tamil" or customer_language == "tam":
            UPI = "யூப்பிஐ"
        elif customer_language == "telugu" or customer_language == "tel":
            UPI = "యూపియయి"
        else:
            UPI = "UPI"
        # UPI = "UPI"
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason == "payment_gateway_issue":
            if delay_reason_needed == "yes":
                template_name = (
                    "utter_payment_gateway_issue_"+emi_flow+"_static" + SRP + bot_gender
                )
                print("The generated template name", template_name)
                dispatcher.utter_template(template_name, tracker)
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Payment Gateway Issue",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
            else:
                return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]
        if eligible == "yes":
            if temp_intent == "ask" and sub_context == "process":
                print("enterint into ask or inform intent with preocess")
                template_name = (
                    "utter_process_pay_via_UPI_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                dispatcher.utter_template(template_name, tracker, user_requested_payment_option=UPI,online_payment_option =UPI,available_payment_mode=payment_method)
            elif temp_intent == "inform" and context == "payment" and sub_context == "action_by_customer" and sub_intent == "affirm" and emi_flow!="predue":
                if len(entities) == 0:
                    dispatcher.utter_template(
                                "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker)
                    print("Entering into AccPTP Affirm")
                    send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=temp_intent.capitalize()+" UPI Payment",disposition_id="APTP",
                            # ptp_date= given_date,
                            flag=TIMEOUT_FLAG,
                        )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
            elif temp_intent == "ask" or temp_intent == "inform":
                print("enterint into ask or inform intent")
                template_name = (
                    "utter_action_by_customer_payment_option_available_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                ) 
                dispatcher.utter_template(template_name, tracker, user_requested_payment_mode=UPI,user_requested_payment_option=UPI,online_payment_option = UPI,available_payment_mode=payment_method)
            
        else:
            if auto_debit=="auto debit":
                template = (
                    "utter_process_payment_option_not_available_noPTPdate_"+auto_debit_nach+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
            else:
                template = (
                    "utter_process_payment_option_not_available_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
            dispatcher.utter_template(
                template,
                tracker,
                user_requested_payment_option="UPI",
                available_payment_mode=payment_method,
            )
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    disposition_details=temp_intent.capitalize()+" UPI Payment",
                    flag=DEFAULT_FLAG,
                )
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    dispatcher.utter_template(
                        "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    )
                    print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" UPI Payment",disposition_id="APTP",
                        ptp_date= given_date,
                        flag=TIMEOUT_FLAG,
                    )
                    return [FollowupAction("action_listen"), AllSlotsReset()]
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=temp_intent.capitalize()+" UPI Payment",disposition_id="UPTP",
                            ptp_date= given_date,
                            flag=DEFAULT_FLAG,)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]
class ActionPaymentMethod(Action):
    def name(self):
        return "action_payment_method"

    def run(self, dispatcher, tracker, domain):
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        entities = tracker.latest_message["entities"]
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        payment_method = paymentMode(tracker,"available_payment_mode")
        bot_gender = tracker.get_slot("bot_gender")
        threshold_days = tracker.get_slot("threshold_days_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        print("The signal", signal)
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        print("The delay_reason", delay_reason)
        if (
            signal == "payment_method"
            # and delay_reason == "no_delay_reason"
            and (context == "payment" or context == "loan")
        ):
            if auto_debit == "auto debit":   
                template_name = (
                    "utter_process_payment_method_noPTPdate_"+auto_debit_nach+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
            else:   
                template_name = (
                    "utter_process_payment_method_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
            print("The generated template name", template_name)
            dispatcher.utter_template(
                template_name, tracker, tracker, available_payment_mode=payment_method
            )
            if len(entities) == 0:
                print("Entering into NoPTP")
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Payment Method",
                    emi_flow=emi_flow,
                )
                return [
                        SlotSet(REQUESTED_SLOT, None),
                        # SlotSet("name_confirmation", "True"),
                        SlotSet("trail_count", 1),
                        FollowupAction(tracker.active_form.get("name")),
                    ]
            else:
                for entity in entities:
                    date_condition = False
                    given_date = ""
                    if entity.get("entity", None) == "date":
                        due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                        if "due_date" in entity["value"]:
                            value = entity["value"].split("due_date")[1]
                            if "-" in value:
                                value  = value.split("-")[1]
                                given_date = due_date - timedelta(days=int(value))
                            elif "+" in value:
                                value = value.split("+")[1]
                                given_date = due_date + timedelta(days=int(value))
                            else:
                                given_date =  due_date
                        else:
                            given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                        if emi_flow == "predue":
                            date_condition = (given_date.date()<= due_date.date())
                        else:
                            no_of_days = given_date.date() - datetime.datetime.now().date()
                            date_condition = (no_of_days.days <= int(threshold_days))
                        given_date = given_date.strftime("%d %B %Y").lstrip('0')
                    for entity in entities:
                        if entity.get("entity", None) == "time":
                            th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                            given_time = entity["value"]
                            th_ptp_time1 = th_ptp_time.split(":")
                            given_date_time = given_date + given_time
                            given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                            print("the given_date_time",given_date_time)
                            if emi_flow == "predue":
                                th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                            else:
                                today = datetime.datetime.now()
                                atp_date = today + timedelta(days=int(threshold_days))
                                th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                            date_condition = (given_date_time <= th_date_time)
                    if date_condition:
                        # dispatcher.utter_template(
                        #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                        # )
                        print("Entering into AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Payment Method",disposition_id="APTP",
                            ptp_date=given_date,
                            flag=DEFAULT_FLAG,
                        )
                        return aptp_decide_slot(tracker)
                    else:
                        if tracker.active_form.get("name") is not None:
                            print("Entering into Not AccPTP")

                            send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Payment Method",
                            ptp_date=given_date,
                            flag=DEFAULT_FLAG)
                            return decide_slot(tracker)
                return [FollowupAction("action_listen")]


class ActionPaymentLaterNotNow(Action):
    def name(self):
        return "action_payment_later_not_now"

    def run(self, dispatcher, tracker, domain):
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        entities = tracker.latest_message["entities"]
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        payment_method = paymentMode(tracker,"available_payment_mode")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        threshold_days = tracker.get_slot("threshold_days_slot")
        entities = tracker.latest_message["entities"]
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        customer_name = tracker.get_slot("customer_name")
        due_date_resposne = tracker.get_slot("due_date")
        emi_amount = tracker.get_slot("emi_amount_slot")
        bank_name = tracker.get_slot("bank_name_slot")
        print("The signal", signal)
        print("The delay_reason", delay_reason)
        print("coming332gg")
        if (
            (signal == "payment_later_not_now")
            and (context == "payment")
        ): 
            if len(entities) == 0:
                if sentiment == "positive" or sentiment == "neutral":
                    if auto_debit == "auto debit":
                        template_name = (
                        "utter_payment_later_not_now_AccPTP_positive_"+auto_debit_nach+emi_flow+"_static"
                        + SRP
                        + bot_gender)
                    else:
                        template_name = (
                            "utter_payment_later_not_now_AccPTP_positive_"+emi_flow+"_static"
                            + SRP
                            + bot_gender)
                elif sentiment == "negative":
                    if auto_debit == "auto debit":
                        template_name = (
                            "utter_payment_later_not_now_AccPTP_negative_"+auto_debit_nach+emi_flow+"_static"
                            + SRP
                            + bot_gender
                        )
                    else:
                        template_name = (
                            "utter_payment_later_not_now_AccPTP_negative_"+emi_flow+"_static"
                            + SRP
                            + bot_gender
                        )
                print("The generated template name", template_name)
                dispatcher.utter_template(
                    template_name, tracker, tracker, available_payment_mode=payment_method,customer_name=customer_name,monthly_emi=emi_amount,monthly_emi_date=due_date_resposne,housing_finance=bank_name
                )
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Pay Later",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
            else:
                for entity in entities:
                    date_condition = False
                    given_date = ""
                    if entity.get("entity", None) == "date":
                        due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                        if "due_date" in entity["value"]:
                            value = entity["value"].split("due_date")[1]
                            if "-" in value:
                                value  = value.split("-")[1]
                                given_date = due_date - timedelta(days=int(value))
                            elif "+" in value:
                                value = value.split("+")[1]
                                given_date = due_date + timedelta(days=int(value))
                            else:
                                given_date =  due_date
                        else:
                            given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                        if emi_flow == "predue":
                            date_condition = (given_date.date()<= due_date.date())
                        else:
                            no_of_days = given_date.date() - datetime.datetime.now().date()
                            date_condition = (no_of_days.days <= int(threshold_days))
                        given_date = given_date.strftime("%d %B %Y").lstrip('0')
                    for entity in entities:
                        if entity.get("entity", None) == "time":
                            th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                            given_time = entity["value"]
                            th_ptp_time1 = th_ptp_time.split(":")
                            given_date_time = given_date + given_time
                            given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                            print("the given_date_time",given_date_time)
                            if emi_flow == "predue":
                                th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                            else:
                                today = datetime.datetime.now()
                                atp_date = today + timedelta(days=int(threshold_days))
                                th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                            date_condition = (given_date_time <= th_date_time)
                    if date_condition:
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Pay Later",disposition_id="APTP",
                            ptp_date= given_date,
                            flag=DEFAULT_FLAG,
                        )
                        return aptp_decide_slot(tracker)
                    else:
                        print("Entering into Not AccPTP")
                        if tracker.active_form.get("name") is not None:
                            send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Pay Later",disposition_id="UPTP",
                            ptp_date=given_date,
                            flag=DEFAULT_FLAG)
                            return decide_slot(tracker)
                return get_return_values(tracker)
        else:
            print("coming765gg")
            send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Pay Later",
                            ptp_date=given_date,
                            flag=DEFAULT_FLAG)
            return decide_slot(tracker)

class ActionLatePayment(Action):
    def name(self):
        return "action_late_payment"

    def run(self, dispatcher, tracker, domain):
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        entities = tracker.latest_message["entities"]
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        payment_method = paymentMode(tracker,"available_payment_mode")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        threshold_days = tracker.get_slot("threshold_days_slot")
        entities = tracker.latest_message["entities"]
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        customer_name = tracker.get_slot("customer_name")
        due_date_resposne = tracker.get_slot("due_date")
        emi_amount = tracker.get_slot("emi_amount_slot")
        bank_name = tracker.get_slot("bank_name_slot")
        print("The signal", signal)
        print("The delay_reason", delay_reason)
        if (
            (signal == "late_payment")
            # and delay_reason == "no_delay_reason"
            and (context == "payment") or (context == "general")
        ): 
            if len(entities) == 0:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Pay Later",
                    emi_flow=emi_flow,
                )
                return aptp_decide_slot(tracker)
            else:
                for entity in entities:
                    date_condition = False
                    given_date = ""
                    if entity.get("entity", None) == "date":
                        due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                        if "due_date" in entity["value"]:
                            value = entity["value"].split("due_date")[1]
                            if "-" in value:
                                value  = value.split("-")[1]
                                given_date = due_date - timedelta(days=int(value))
                            elif "+" in value:
                                value = value.split("+")[1]
                                given_date = due_date + timedelta(days=int(value))
                            else:
                                given_date =  due_date
                        else:
                            given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                        if emi_flow == "predue":
                            date_condition = (given_date.date()<= due_date.date())
                        else:
                            no_of_days = given_date.date() - datetime.datetime.now().date()
                            date_condition = (no_of_days.days <= int(threshold_days))
                        given_date = given_date.strftime("%d %B %Y").lstrip('0')
                    for entity in entities:
                        if entity.get("entity", None) == "time":
                            th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                            given_time = entity["value"]
                            th_ptp_time1 = th_ptp_time.split(":")
                            given_date_time = given_date + given_time
                            given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                            print("the given_date_time",given_date_time)
                            if emi_flow == "predue":
                                th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                            else:
                                today = datetime.datetime.now()
                                atp_date = today + timedelta(days=int(threshold_days))
                                th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                            date_condition = (given_date_time <= th_date_time)
                    if date_condition:
                        # dispatcher.utter_template(
                        #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                        # )
                        # print("Entering into AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Pay Later",disposition_id="APTP",
                            ptp_date= given_date,
                            flag=DEFAULT_FLAG,
                        )
                        return aptp_decide_slot(tracker)
                    else:
                        if tracker.active_form.get("name") is not None:
                            print("Entering into Not AccPTP")

                            send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Pay Later",disposition_id="UPTP",
                            ptp_date=given_date,
                            flag=DEFAULT_FLAG)
                            return decide_slot(tracker)
                return get_return_values(tracker)



class ActionLoanTenureLeft(Action):
    def name(self):
        return "action_loan_tenure_left"

    def run(self, dispatcher, tracker, domain):
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        entities = tracker.latest_message["entities"]
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        payment_method = paymentMode(tracker,"available_payment_mode")
        bot_gender = tracker.get_slot("bot_gender")
        threshold_days = tracker.get_slot("threshold_days_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        loan_end_date = tracker.get_slot("loan_end_date_slot")
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        if loan_end_date != "":
            loan_end_date = datetime.datetime.strptime(loan_end_date, "%d-%m-%Y")
            loan_end_date = loan_end_date.strftime("%d %B %Y").lstrip('0')
        else:
            loan_end_date = loan_end_date
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        tenure_left = tracker.get_slot("tenure_left")
        print("The signal", signal)
        print("The delay_reason", delay_reason)
        print("bot_gender1212", bot_gender)
        if (
            (signal == "loan_tenure_left")
            and(delay_reason == "no_delay_reason")
            and (context == "loan" or context == "general" or context == "payment")
        ):
            if tenure_left != "":
                template_name = (
                    "utter_action_by_bot_tenure_left_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender
                )
                print("The generated template name", template_name)
                dispatcher.utter_template(
                    template_name,
                    tracker,
                    tracker,
                    loan_end_date=loan_end_date,
                    no_of_EMIs_pending=tenure_left,
                )
            else:
                dispatcher.utter_template(
                    "utter_quantitative_data_alt_response_"+emi_flow+"_static"
                    + SRP
                    + bot_gender,
                    tracker)
            if len(entities) == 0:
                print("Entering into NoPTP")
                send_and_store_disposition_details(
                                tracker=tracker,
                                dispatcher=dispatcher,
                                disposition_details=intent.capitalize()+" Loan Tenure",
                                flag=DEFAULT_FLAG,
                            )
                return get_return_values(tracker)
            else:
                for entity in entities:
                    date_condition = False
                    given_date = ""
                    if entity.get("entity", None) == "date":
                        due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                        if "due_date" in entity["value"]:
                            value = entity["value"].split("due_date")[1]
                            if "-" in value:
                                value  = value.split("-")[1]
                                given_date = due_date - timedelta(days=int(value))
                            elif "+" in value:
                                value = value.split("+")[1]
                                given_date = due_date + timedelta(days=int(value))
                            else:
                                given_date =  due_date
                        else:
                            given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                        if emi_flow == "predue":
                            date_condition = (given_date.date()<= due_date.date())
                        else:
                            no_of_days = given_date.date() - datetime.datetime.now().date()
                            date_condition = (no_of_days.days <= int(threshold_days))
                        given_date = given_date.strftime("%d %B %Y").lstrip('0')
                    for entity in entities:
                        if entity.get("entity", None) == "time":
                            th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                            given_time = entity["value"]
                            th_ptp_time1 = th_ptp_time.split(":")
                            given_date_time = given_date + given_time
                            given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                            print("the given_date_time",given_date_time)
                            if emi_flow == "predue":
                                th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                            else:
                                today = datetime.datetime.now()
                                atp_date = today + timedelta(days=int(threshold_days))
                                th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                            date_condition = (given_date_time <= th_date_time)
                    if date_condition:
                        # dispatcher.utter_template(
                        #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                        # )
                        # print("Entering into AccPTP")
                        send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Loan Tenure",disposition_id="APTP",
                            ptp_date= given_date,
                            flag=DEFAULT_FLAG,
                        )
                        return aptp_decide_slot(tracker)
                    else:
                        if tracker.active_form.get("name") is not None:
                            print("Entering into Not AccPTP")

                            send_and_store_disposition_details(
                            tracker=tracker,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Loan Tenure",disposition_id="UPTP",
                            ptp_date=given_date,
                            flag=DEFAULT_FLAG)
                            return decide_slot(tracker)
                return [FollowupAction("action_listen")]


class Actioncredit_score(Action):
    def name(self):
        return "action_credit_score"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        template_name = (
            "utter_action_by_client_noPTPdate_"+emi_flow+"_static" + SRP + bot_gender
        )
        print("The generated template name", template_name)
        dispatcher.utter_template(template_name, tracker)
        send_and_store_disposition_details(
            tracker=tracker,
            flag=DEFAULT_FLAG,
            dispatcher=dispatcher,
            disposition_details=intent.capitalize()+" Credit Score",
            emi_flow=emi_flow,
        )
        if len(entities) == 0:
            print("Entering into NoPTP")
            return get_return_values(tracker)
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    # print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Credit Score",disposition_id="APTP",
                        ptp_date=given_date,
                        flag=DEFAULT_FLAG,
                    )
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")

                        send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Credit Score",disposition_id="UPTP",
                        ptp_date=given_date,
                        flag=DEFAULT_FLAG,)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]

class ActionEmiDetails(Action):
    def name(self):
        return "action_emi_details"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        bank_name = tracker.get_slot("bank_name_slot")
        principal_amount = tracker.get_slot("principal_amount_slot")
        SRP = SRP_value(customer_language,region)
        emi_amount = tracker.get_slot("emi_amount_slot")
        signal = tracker.latest_message.get("signal").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        variation = tracker.get_slot("variation_slot")
        print("comndkqd")
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if signal == "emi_details" and sub_context == "issue":
                template_name = (
                    "utter_issue_customer_or_account_details_"+emi_flow+"_static"+ SRP+bot_gender
                )
                print("The generated template name", template_name)
                dispatcher.utter_template(template_name, tracker)
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="General - Inform Issue",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
        if signal == "emi_details" and sub_context == "general":
                dispatcher.utter_template(
                    "utter_action_by_bot_client_name_noPTPdate_"+emi_flow+"_static"
                    + SRP
                    + bot_gender,
                    tracker,
                    principal_amount=principal_amount,
                    client_name=bank_name,
                )
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Loan Information",
                    emi_flow=emi_flow,
                )
                return get_return_values(tracker)
        if signal == "emi_details" and (sub_context == "action_by_bot" or sub_context == "quantitative_data") :
            dispatcher.utter_template(
                "utter_action_by_bot_emi_amount_noPTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker,
                monthly_emi=emi_amount,
            )
            send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" EMI Amount",
                        flag=DEFAULT_FLAG,
                        emi_flow=emi_flow)
            return get_return_values(tracker)
        
        if delay_reason_needed == "yes":
            if signal == "emi_details" and delay_reason == "emi_date_not_informed":
                dispatcher.utter_template(
                    "utter_emi_date_not_confirmed_"+variation+emi_flow+"_"
                    + region
                    + gender
                    + age_category
                    + collared
                    + "_"
                    + typology
                    + bot_gender,
                    tracker,
                )
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Date Not Informed",
                    emi_flow=emi_flow,
                )
                return [FollowupAction("action_listen"), AllSlotsReset()]
            
            
            # else:
            #     send_and_store_disposition_details(
            #         tracker=tracker,
            #         flag=DEFAULT_FLAG,
            #         dispatcher=dispatcher,
            #         disposition_details="General - Inform Issue",
            #         emi_flow=emi_flow,
            #     )
            # return get_return_values(tracker)
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]


class ActionPartialPayment(Action):
    def name(self):
        return "action_partial_payment"
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        partial_payment = tracker.get_slot("partial_payment")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        sms_integration = tracker.get_slot("sms_integration_slot")
        partial_payment_slot = tracker.get_slot("partial_payment_slot")
        emi_amount = tracker.get_slot("emi_amount_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        minimum_pp_emi_amount = tracker.get_slot("minimum_pp_emi_amount_slot")
        maximum_pp_emi_amount = tracker.get_slot("maximum_pp_emi_amount_slot")
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        payment_method = paymentMode(tracker,"available_payment_mode")
        due_date = tracker.get_slot("due_date_without_formatting_slot")
        customer_name = tracker.get_slot("customer_name")
        due_date_resposne = tracker.get_slot("due_date")
        bank_name = tracker.get_slot("bank_name_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        print("The value od req slot",REQUESTED_SLOT2)  
        print("The value od req slot",partial_payment_slot)
        if partial_payment_slot == "yes" and (emi_flow != "predue" or  emi_flow !="duedate"):
            if entities:
                for entity in entities:
                    given_date = datetime.date.today()
                    date_condition = False
                    amount_condition = False
                    if entity.get("entity", None) == "date":
                        if "due_date" in entity["value"]:
                            value = entity["value"].split("due_date")[1]
                            if "-" in value:
                                value  = value.split("-")[1]
                                date = datetime.datetime.strptime(due_date, "%d-%m-%Y")
                                given_date = date - timedelta(days=int(value))
                            elif "+" in value:
                                value = value.split("+")[1]
                                date = datetime.datetime.strptime(due_date, "%d-%m-%Y")
                                given_date = date + timedelta(days=int(value))
                            else:
                                given_date =  datetime.datetime.strptime(due_date, "%d-%m-%Y")
                        else:
                            given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                        due_date= datetime.datetime.strptime(due_date,"%d-%m-%Y")
                        if emi_flow == "predue":
                            print("the given date",given_date)
                            print("the due_date",due_date)
                            date_condition = (given_date.date()<= due_date.date())
                        else:
                            no_of_days = given_date.date() - datetime.datetime.now().date()
                            print("no_of_days", no_of_days.days)
                            date_condition = (no_of_days.days <= int(threshold_days))
                    if entity.get("entity", None) == "number" and int(entity.get("value", None)) > 31:
                        given_amount = int(entity["value"])
                        if given_amount >= int(emi_amount):
                            amount_condition = "total"
                        elif level_of_negotiation == "1" and (given_amount >= int(minimum_pp_emi_amount)):
                            amount_condition = "pp"
                        elif level_of_negotiation == "2" and (given_amount >= int(maximum_pp_emi_amount)):
                            amount_condition = "pp"
                        else:
                            amount_condition = False    
                    print("amount_condition: ",amount_condition)
                    if amount_condition == "total" and date_condition:
                        send_and_store_disposition_details(
                            tracker=tracker,dispatcher=dispatcher,flag=DEFAULT_FLAG,disposition_id="ATP")
                        return aptp_decide_slot(tracker)
                    elif amount_condition == "pp" and date_condition:
                        if sms_integration == "yes":
                            dispatcher.utter_template("utter_affirm_SMS_configured_slot_1_"+emi_flow+"_static"+ SRP+ bot_gender,tracker)
                        else:
                            dispatcher.utter_template("utter_affirm_SMS_not_Configured_slot_1_"+emi_flow+"_static"+ SRP+ bot_gender,tracker)
                        send_and_store_disposition_details(tracker=tracker, dispatcher=dispatcher, flag=TIMEOUT_FLAG,disposition_id="Minimum Amount Due Accepted",disposition_details="User")
                        return [FollowupAction("action_listen"), AllSlotsReset()]
                    else:
                        return [FollowupAction("partial_payment_lvl1_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),SlotSet("changing_slot",str(REQUESTED_SLOT2)),]
            else:
                return [FollowupAction("partial_payment_lvl1_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),SlotSet("changing_slot",str(REQUESTED_SLOT2)),]
        else: #partial_payment_slot = "no"
            print("enterted into main response submit ")
            dispatcher.utter_template("utter_partial_payment_not_supported_"+emi_flow+"_static"+SRP+bot_gender,tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=DEFAULT_FLAG,
                dispatcher=dispatcher,
                disposition_details="General - Partial Payment Not Supported",
                emi_flow=emi_flow,
            )
            return get_return_values(tracker)
class ActionLoanCompleted(Action):
    def name(self):
        return "action_loan_completed"
    
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        template_name = (
            "utter_account_closed_"+emi_flow+"_static" + SRP + bot_gender
        )
        print("The generated template name", template_name)
        dispatcher.utter_template(template_name, tracker)
        send_and_store_disposition_details(
            tracker=tracker,
            flag=TIMEOUT_FLAG,
            dispatcher=dispatcher,
            disposition_details="General - Loan Completed",
            emi_flow=emi_flow,
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]

class ActionProductDetail(Action):
    def name(self):
        return "action_product_detail"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        principal_amount_slot = tracker.get_slot("principal_amount_slot")
        client_name_slot = tracker.get_slot("client_name_slot")
        bank_name = tracker.get_slot("bank_name_slot")
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        if principal_amount_slot != "":
            template_name = (
                "utter_action_by_bot_client_name_noPTPdate_"+emi_flow+"_static" + SRP + bot_gender
            )
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker,principal_amount = principal_amount_slot,client_name = bank_name)
        else:
            dispatcher.utter_template(
                "utter_quantitative_data_alt_response_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
        if len(entities) == 0:
            print("Entering into NoPTP")
            if tracker.active_form.get("name") is not None:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=DEFAULT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details=intent.capitalize()+" Loan Information",
                    emi_flow=emi_flow)
                return get_return_values(tracker)
            return [FollowupAction("action_listen")]
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    # print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        flag=DEFAULT_FLAG,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Loan Information",disposition_id="APTP",
                        ptp_date= given_date,
                        emi_flow=emi_flow)
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")

                        send_and_store_disposition_details(
                            tracker=tracker,
                            flag=DEFAULT_FLAG,
                            dispatcher=dispatcher,
                            disposition_details=intent.capitalize()+" Loan Information",disposition_id="UPTP",
                            ptp_date=given_date,
                            emi_flow=emi_flow)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]
class ActionCustomerName(Action):
    def name(self):
        return "action_customer_name"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        principal_amount_slot = tracker.get_slot("principal_amount_slot")
        client_name_slot = tracker.get_slot("client_name_slot")
        bank_name = tracker.get_slot("bank_name_slot")
        entities = tracker.latest_message["entities"]
        account_name = tracker.get_slot("account_name_slot")
        script_type = tracker.get_slot("script_type_slot")
        print("commmingngng")
        if account_name == "Ring" or account_name == "Ring Testing" and  (script_type == "short"):
            return [FollowupAction("thirdparty_level1_x2_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
        if account_name == "Axio" or account_name == "Axio Testing" or account_name == "SmartCoin" or account_name == "SmartCoin Testing" or account_name == "TVS Credit Collections Testing" or account_name == "TVS Credit Collections":
            return [FollowupAction("thirdparty_old_level1_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
        elif account_name == "Shriram Housing" or account_name == "Shriram Housing Testing":
            return [FollowupAction("thirdparty_level1_x_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
        else:
            return [FollowupAction("thirdparty_level1_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]

        

class ActionPaymentdateExtension(Action):
    def name(self):
        return "action_payment_date_extension"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        print("coming 7217",signal)
        template_name = (
            "utter_action_by_client_noPTPdate_"+emi_flow+"_static" + SRP + bot_gender
        )
        print("The generated template name", template_name)
        dispatcher.utter_template(template_name, tracker)
        send_and_store_disposition_details(
            tracker=tracker,
            flag=DEFAULT_FLAG,
            dispatcher=dispatcher,
            disposition_details="General - Payment Date Extension",
            emi_flow=emi_flow,
        )
        return get_return_values(tracker)


class ActionApplicationIssue(Action): ##
    def name(self):
        return "action_application_issue"
    
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        # intent = tracker.latest_message.get("temp_intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = (
                "utter_client_or_application_issue_"+emi_flow+"_static" + SRP + bot_gender
            )
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_details="Delay - Application Issue",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]

class ActionCustomerCareConnect(Action):
    def name(self):
        return "action_customer_care_contact_info"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        dispatcher.utter_template(
                        "utter_customer_care_contact_"+emi_flow+"_static" + SRP + bot_gender,
                        tracker,
                    )
        send_and_store_disposition_details(
            tracker=tracker,
            flag=TIMEOUT_FLAG,
            dispatcher=dispatcher,
            disposition_details="General - Customer Care Contact",
            emi_flow=emi_flow,
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]

class ActionUserCallLater(Action):
    def name(self):
        return "action_user_call_later"
    
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        customer_name = tracker.get_slot("customer_name")
        due_date_resposne = tracker.get_slot("due_date")
        emi_amount = tracker.get_slot("emi_amount_slot")
        bank_name = tracker.get_slot("bank_name_slot")
        dispatcher.utter_template(
                    "utter_customer_call_later_"+emi_flow+"_static" + SRP + bot_gender, tracker,customer_name=customer_name,monthly_emi=emi_amount,monthly_emi_date=due_date_resposne,housing_finance=bank_name)
        send_and_store_disposition_details(
            tracker=tracker,
            dispatcher=dispatcher,
            flag=TIMEOUT_FLAG,
            disposition_details="General - Customer Call Later",
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]

class ActionWrongNumber(Action):
    def name(self):
        return "action_wrong_number"
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        customer_name = tracker.get_slot("customer_name")
        due_date_resposne = tracker.get_slot("due_date")
        emi_amount = tracker.get_slot("emi_amount_slot")
        bank_name = tracker.get_slot("bank_name_slot")
        dispatcher.utter_template(
                    "utter_deny_wrong_number_"+emi_flow+"_static" + SRP + bot_gender, tracker,customer_name=customer_name,monthly_emi=emi_amount,monthly_emi_date=due_date_resposne,housing_finance=bank_name
                )
        send_and_store_disposition_details(
            tracker=tracker,
            dispatcher=dispatcher,
            flag=TIMEOUT_FLAG,
            disposition_details="General - Wrong Number",
            disposition_id = "Dispute"
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]

    
class ActionWrongLoanID(Action):
    def name(self):
        return "action_wrong_loan_id"
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        signal = tracker.latest_message.get("signal").get("name")

        if (sub_context == "issue" or sub_context == "general") and (context == "loan" or context == "bank_account") and signal == "wrong_loan_id":
            dispatcher.utter_template(
                    "utter_issue_customer_or_account_details_"+emi_flow+"_static"
                    + SRP
                    + bot_gender,
                    tracker,
                )
            send_and_store_disposition_details(
                    tracker=tracker, dispatcher=dispatcher, flag=TIMEOUT_FLAG,disposition_details="General - Wrong Loan",disposition_id = "Dispute"
                )
            return [FollowupAction("action_listen"), AllSlotsReset()]
    
class ActionWillPayLateFee(Action):
    def name(self):
        return "action_will_pay_late_fee"

    def run (self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        signal = tracker.latest_message.get("signal").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        gender = tracker.get_slot("gender_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        bot_gender = tracker.get_slot("bot_gender")
        late_fees = tracker.get_slot("late_fee_percentage_slot")
        intent = tracker.latest_message.get("temp_intent").get("name")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        due_date = tracker.get_slot("due_date_without_formatting_slot")
        print("late_fees222",late_fees)
        if late_fees != "":
            dispatcher.utter_template(
                "utter_quantitative_data_late_fees_PTPdate_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker,
                late_fee_percentage=late_fees,
            )
        else:
            dispatcher.utter_template(
                "utter_quantitative_data_alt_response_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
        send_and_store_disposition_details(
                    tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG,disposition_details="General - Pay Late Fee"
                )
        return [
                SlotSet(REQUESTED_SLOT, None),
                FollowupAction(tracker.active_form.get("name")),
        ]
        

class ActionCurrentInterestRate(Action):
    def name(self):
        return "action_current_interest_rate"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        template_name = (
            "utter_action_by_client_noPTPdate_"+emi_flow+"_static" + SRP + bot_gender
        )
        print("The generated template name", template_name)
        dispatcher.utter_template(template_name, tracker)
        send_and_store_disposition_details(
            tracker=tracker,
            flag=DEFAULT_FLAG,
            dispatcher=dispatcher,
            disposition_details=intent.capitalize()+" Interest Rate",
            emi_flow=emi_flow,
        )
        if len(entities) == 0:
            print("Entering into NoPTP")
            return get_return_values(tracker)
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    # print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Interest Rate",disposition_id="APTP",
                        ptp_date=given_date,
                        flag=DEFAULT_FLAG,
                    )
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Interest Rate",disposition_id="UPTP",
                        ptp_date=given_date,
                        flag=DEFAULT_FLAG)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]

class ActionTotalLoanAmount(Action):
    def name(self):
        return "action_total_loan_amount"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("temp_intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        threshold_days = tracker.get_slot("threshold_days_slot")
        due_date_without_formatting = tracker.get_slot("due_date_without_formatting_slot")
        total_loan_amount = tracker.get_slot("total_loan_amount_slot")
        print("total_loan_amount6700",total_loan_amount)
        REQUESTED_SLOT2 = tracker.get_slot(REQUESTED_SLOT)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        if total_loan_amount != "":
            template_name = (
            "utter_quantitative_data_total_loan_amount_PTPdate_"+emi_flow+"_static" + SRP + bot_gender)
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker,total_loan_amount=total_loan_amount)
        else:
            dispatcher.utter_template(
                "utter_quantitative_data_alt_response_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
        send_and_store_disposition_details(
            tracker=tracker,
            flag=DEFAULT_FLAG,
            dispatcher=dispatcher,
            disposition_details=intent.capitalize()+" Loan Amount",
            emi_flow=emi_flow,
        )
        if len(entities) == 0:
            print("Entering into NoPTP")
            return get_return_values(tracker)
        else:
            for entity in entities:
                date_condition = False
                given_date = ""
                if entity.get("entity", None) == "date":
                    due_date = datetime.datetime.strptime(due_date_without_formatting,"%d-%m-%Y")
                    if "due_date" in entity["value"]:
                        value = entity["value"].split("due_date")[1]
                        if "-" in value:
                            value  = value.split("-")[1]
                            given_date = due_date - timedelta(days=int(value))
                        elif "+" in value:
                            value = value.split("+")[1]
                            given_date = due_date + timedelta(days=int(value))
                        else:
                            given_date =  due_date
                    else:
                        given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y")
                    if emi_flow == "predue":
                        date_condition = (given_date.date()<= due_date.date())
                    else:
                        no_of_days = given_date.date() - datetime.datetime.now().date()
                        date_condition = (no_of_days.days <= int(threshold_days))
                    given_date = given_date.strftime("%d %B %Y").lstrip('0')
                for entity in entities:
                    if entity.get("entity", None) == "time":
                        th_ptp_time = tracker.get_slot("th_ptp_time_slot")
                        given_time = entity["value"]
                        th_ptp_time1 = th_ptp_time.split(":")
                        given_date_time = given_date + given_time
                        given_date_time = datetime.datetime.strptime(given_date_time,"%d %B %Y%H:%M")
                        print("the given_date_time",given_date_time)
                        if emi_flow == "predue":
                            th_date_time =  due_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]))
                        else:
                            today = datetime.datetime.now()
                            atp_date = today + timedelta(days=int(threshold_days))
                            th_date_time =  atp_date.replace(hour=int(th_ptp_time1[0]), minute=int(th_ptp_time1[1]),second=0,microsecond=0)
                        date_condition = (given_date_time <= th_date_time)
                if date_condition:
                    # dispatcher.utter_template(
                    #     "utter_AccPTP_"+auto_debit_nach+emi_flow+"_static" + SRP + bot_gender, tracker
                    # )
                    # print("Entering into AccPTP")
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Loan Amount",disposition_id="APTP",
                        ptp_date=given_date,
                        flag=DEFAULT_FLAG,
                    )
                    return aptp_decide_slot(tracker)
                else:
                    if tracker.active_form.get("name") is not None:
                        print("Entering into Not AccPTP")
                        send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Loan Amount",disposition_id="UPTP",
                        ptp_date=given_date,
                        flag=DEFAULT_FLAG)
                        return decide_slot(tracker)
            return [FollowupAction("action_listen")]

class ActionCurfew(Action):
    def name (self):
        return "action_curfew"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = (
                    "utter_natural_disaster_"+emi_flow+"_static" + SRP + bot_gender
                )
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            if delay_reason == "curfew":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Curfew",
                    emi_flow=emi_flow,
                )
            else:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Natural Disaster",
                    emi_flow=emi_flow,
                )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]
class ActionTransferAccountToAnotherHFC(Action):
    def name(self):
        return "action_transfer_to_another_hfc"

    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        
        template_name = (
            "utter_customer_care_contact_"+emi_flow+"_static" + SRP + bot_gender
        )
        print("The generated template name", template_name)
        dispatcher.utter_template(template_name, tracker)
        send_and_store_disposition_details(
            tracker=tracker,
            flag=TIMEOUT_FLAG,
            dispatcher=dispatcher,
            disposition_details="Delay - Natural Disaster",
            emi_flow=emi_flow,
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]
class ActionDoNotWantToBot(Action):
    def name (self):
        return "action_donot_want_to_talk_to_bot"
        
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        agent_desktop = tracker.get_slot("agent_desktop_slot")
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        if agent_desktop == "yes":
            if sub_intent == "general_ask_inform" or sub_intent == "affirm":
                dispatcher.utter_template("utter_affirm_speak_executive_"+emi_flow+"_static"+SRP+bot_gender,tracker)
                send_and_store_disposition_details(
                    tracker=tracker,dispatcher=dispatcher,flag=HANDOFF_FLAG,
                    disposition_id="Human Handoff Requested",disposition_details="Agent Desktop Available")
                return [FollowupAction("action_listen"), AllSlotsReset()]
            else:
                return get_return_values(tracker)
        else:
            dispatcher.utter_template("utter_customer_care_contact_"+emi_flow+"_static" + SRP + bot_gender, tracker)
            send_and_store_disposition_details(
                tracker=tracker,
                flag=TIMEOUT_FLAG,
                dispatcher=dispatcher,
                disposition_id="Human Handoff Requested",
                disposition_details="Agent Desktop Unavailable",
                emi_flow=emi_flow,
            )
            return [FollowupAction("action_listen"), AllSlotsReset()]

class ActionDeviceLost(Action):
    def name (self):
        return "action_device_lost"
        
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        intent = tracker.latest_message.get("intent").get("name")
        context = tracker.latest_message.get("context").get("name")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        delay_reason_needed= tracker.get_slot("delay_reason_needed_slot")
        if delay_reason_needed == "yes":
            template_name = (
                "utter_data_lost_"+emi_flow+"_static" + SRP + bot_gender
            )
            print("The generated template name", template_name)
            dispatcher.utter_template(template_name, tracker)
            if delay_reason == "device_lost":
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Device Lost",
                    emi_flow=emi_flow,
                )
            else:
                send_and_store_disposition_details(
                    tracker=tracker,
                    flag=TIMEOUT_FLAG,
                    dispatcher=dispatcher,
                    disposition_details="Delay - Data Lost",
                    emi_flow=emi_flow,
                )
            return [FollowupAction("action_listen"), AllSlotsReset()]
        else:
            return [FollowupAction("counselling_v2_form"),SlotSet("trail_count", 5), SlotSet(REQUESTED_SLOT,None)]

class ActionBotCallLater(Action):
    def name(self):
        return "action_bot_call_later"#& busy
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        region = tracker.get_slot("region")
        customer_language = tracker.get_slot("customer_language_slot")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        due_date = tracker.get_slot("due_date_without_formatting_slot")
        threshold_time = tracker.get_slot("threshold_time_slot")
        threshold_time_1 = tracker.get_slot("call_back_time_slot_1")
        call_back_days = tracker.get_slot("call_back_days_slot")
        user_message = tracker.latest_message.get("text")
        due_date_resposne = tracker.get_slot("due_date")
        emi_amount = tracker.get_slot("emi_amount_slot")
        bank_name = tracker.get_slot("bank_name_slot")
        customer_name = tracker.get_slot("customer_name")
        account_name = tracker.get_slot("account_name_slot")
        script_type = tracker.get_slot("script_type_slot")
        print("script_type123432",script_type)
        third_person = tracker.latest_message.get("third_person").get("name")
        print('account_name123654',account_name)
        if third_person == "yes":   #Third Party
            if account_name == "Axio" or account_name == "Axio Testing" or account_name == "SmartCoin" or account_name == "SmartCoin Testing" or account_name == "TVS Credit Collections Testing" or account_name == "TVS Credit Collections":
                return [FollowupAction("thirdparty_old_level1_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
            elif account_name == "Shriram Housing" or account_name == "Shriram Housing Testing":
                return [FollowupAction("thirdparty_level1_x_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
            elif (account_name == "Ring" or account_name == "Ring Testing") and  (script_type == "short"):
                print("435def")
                return [FollowupAction("thirdparty_level1_x2_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
            else:
                return [FollowupAction("thirdparty_level1_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
        if account_name == "Axio" or account_name == "Axio Testing" or account_name == "SmartCoin" or account_name == "SmartCoin Testing" or account_name == "TVS Credit Collections Testing" or account_name == "TVS Credit Collections":
            print("Axio")
            print('cominghdfhd3234k')
            if entities:
                for entity in entities:
                    if entity.get("entity", None) == "date":
                        duedate = datetime.datetime.strptime(due_date, "%d-%m-%Y").date()
                        print("duedate",duedate)
                        today = datetime.date.today()
                        print("today",today)
                        if "due_date" in entity["value"]:
                            value = entity["value"].split("due_date")[1]
                            if entity["value"]=="due_date":
                                given_date = duedate
                            elif "+" in value:
                                value = value.split("+")[1]
                                given_date = duedate + timedelta(days=int(value))
                            else: #elif "-" in value:
                                value  = value.split("-")[1]
                                given_date = duedate - timedelta(days=int(value))
                                print("1344given_date",given_date)
                        else:
                            given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y").date()
                        if emi_flow == "predue":
                            if  given_date == today:
                                date = "today"
                            elif given_date < duedate:
                                date = "true"
                            else:
                                date = "false"
                        else:
                            if  given_date == today:
                                date = "today"
                            else:
                                no_of_days = given_date - today
                                print("no_of_days1212",no_of_days)
                                print("call_back_days",call_back_days)
                                if no_of_days.days <= int(call_back_days):
                                    date = "true"
                                    print("date212",date)
                                else:
                                    date = "false"
                        print("date",date,type(date))
                        date1 = entities[0]["value"]
                        if  len(entities)>1 and entities[1]["entity"] == "time" :
                            print("IN time yes")
                            time1 = entities[1]["value"]
                            given_time_temp =  entities[1]["value"]
                            given_time1 = entities[1]["value"]
                            # print("1378given_time",type(given_time),given_time)
                            given_time = given_time1.split(":")
                            given_time_1 = given_time1.split(":")[0]
                            print("1380given_time",type(given_time),given_time)
                            threshold_time1 = threshold_time.split(":")
                            threshold_time_2 = threshold_time.split(":")[0]
                            now = datetime.datetime.now()
                            print("1383now",type(now),now)
                            print("THrehold time",threshold_time1)
                            given_time = now.replace(hour=int(given_time[0]), minute=int(given_time[1]),second=0,microsecond=0)
                            
                            threshold_time1 = now.replace(hour=int(threshold_time[0]), minute=int(threshold_time[1]))
                            callback_time = date1+" "+time1
                            print("given_time",given_time)
                            print("threshold_time",threshold_time1)
                            if int(given_time_1) <= int(threshold_time_2):   #Acc Time
                                print("Acc Time")
                                if int(given_time_1) >12:
                                    given_time_1 =int(given_time_1)-12
                                if date == "today" or date == "true":
                                    print("Same day,Acc time")  #---->1
                                    dispatcher.utter_template("utter_bot_call_later_time_available_2_"+emi_flow+"_static"+SRP+bot_gender,tracker,callback_time=int(given_time_1))
                                    send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Available",flag=TIMEOUT_FLAG,emi_flow=emi_flow,callback_time = callback_time)
                                    return [FollowupAction("action_listen"), AllSlotsReset()]
                                else:
                                    print("UN DATE,Acc")            #---->2
                                    send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Unavailable",flag=DEFAULT_FLAG,emi_flow=emi_flow,callback_time=callback_time)
                                    return [
                                        FollowupAction("callback_old_level2_form"),
                                        SlotSet(REQUESTED_SLOT, None),
                                        SlotSet("trail_count", None),
                                        SlotSet("go_to_form_slot",None),
                                    ]
                            else:                               #UnAcc Time
                                print("Un Time")
                                if date == "today":
                                    print("Same day,UN time")   #---->3 
                                    dispatcher.utter_template("utter_time_greaterthan_sameday_threshold_3_"+emi_flow+"_static"+SRP+bot_gender,tracker,Threshold_time=threshold_time_1)
                                    send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Unavailable",flag=TIMEOUT_FLAG,emi_flow=emi_flow,callback_time = callback_time)
                                    return [FollowupAction("action_listen"), AllSlotsReset()]
                                elif  date == "true":
                                    print("Acc date,UN time")   #---->5
                                    dispatcher.utter_template("utter_time_greaterthan_threshold_3_"+emi_flow+"_static"+SRP+bot_gender,tracker,Threshold_time=threshold_time_1)
                                    send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Unavailable",flag=TIMEOUT_FLAG,emi_flow=emi_flow,callback_time = callback_time)
                                    return [FollowupAction("action_listen"), AllSlotsReset()]
                                else:
                                    print("UN DATE")            #---->2
                                    send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Unavailable",flag=DEFAULT_FLAG,emi_flow=emi_flow,callback_time=callback_time)
                                    return [
                                        FollowupAction("callback_old_level2_form"),
                                        SlotSet(REQUESTED_SLOT, None),
                                        SlotSet("trail_count", None),
                                        SlotSet("go_to_form_slot",None),
                                    ]
                        else:
                            print("IN only date")
                            callback_time = date1
                            if date == "today" or date == "true":
                                print("Same day,No time")       #---->1
                                dispatcher.utter_template("utter_time_lesserthan_threshold_2_"+emi_flow+"_static"+SRP+bot_gender,tracker)
                                send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Available",flag=TIMEOUT_FLAG,emi_flow=emi_flow,callback_time = callback_time)
                                return [FollowupAction("action_listen"), AllSlotsReset()]
                            else:
                                print("UN DATE")                #---->2
                                send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Unavailable",flag=DEFAULT_FLAG,emi_flow=emi_flow,callback_time=callback_time)
                                return [
                                        FollowupAction("callback_old_level2_form"),
                                        SlotSet(REQUESTED_SLOT, None),
                                        SlotSet("trail_count", None),
                                        SlotSet("go_to_form_slot",None),
                                    ]
            else:
                print("NO Date,No Time") 
                print('cominghdfhd6677k')                           #---->4
                send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Unavailable",flag=DEFAULT_FLAG,emi_flow=emi_flow)
                return [
                            FollowupAction("callback_old_level1_form"),
                            SlotSet(REQUESTED_SLOT, None),
                            SlotSet("trail_count", None),
                            SlotSet("go_to_form_slot",None),
                        ]
        else:
            if account_name == "PayTM Testing" or account_name == "PayTM":
                callback_level1_form = "callback_level1_form"
                callback_level2_form = "callback_level2_x_form"
            elif (((account_name == "Ring" or account_name == "Ring Testing") and (script_type == "short"))
                  or (account_name == "Sonata Finance" or account_name == "Sonata Finance Testing")
                ):
                callback_level1_form = "callback_level1_x_form"
                callback_level2_form = "callback_level1_x_form"
            else:
                print("fjwojfowj")
                callback_level1_form = "callback_level1_form"
                callback_level2_form = "callback_level2_form"
            if entities:
                print("heree48374389")
                for entity in entities:
                    if entity.get("entity", None) == "date":
                        duedate = datetime.datetime.strptime(due_date, "%d-%m-%Y").date()
                        print("duedate",duedate)
                        today = datetime.date.today()
                        print("today",today)
                        if "due_date" in entity["value"]:
                            value = entity["value"].split("due_date")[1]
                            if entity["value"]=="due_date":
                                given_date = duedate
                            elif "+" in value:
                                value = value.split("+")[1]
                                given_date = duedate + timedelta(days=int(value))
                            else: #elif "-" in value:
                                value  = value.split("-")[1]
                                given_date = duedate - timedelta(days=int(value))
                                print("1344given_date",given_date)
                        else:
                            given_date = datetime.datetime.strptime(entity["value"], "%d/%m/%Y").date()
                        if emi_flow == "predue":
                            if  given_date == today:
                                date = "today"
                            elif given_date < duedate:
                                date = "true"
                            else:
                                date = "false"
                        else:
                            if  given_date == today:
                                date = "today"
                            else:
                                no_of_days = given_date - today
                                if no_of_days.days <= int(call_back_days):
                                    date = "true"
                                else:
                                    date = "false"
                        print("date",date,type(date))
                        date1 = entities[0]["value"]
                        if  len(entities)>1 and entities[1]["entity"] == "time" :
                            print("IN time yes")
                            time1 = entities[1]["value"]
                            given_time_temp =  entities[1]["value"]
                            given_time1 = entities[1]["value"]
                            given_time = given_time1.split(":")
                            given_time_1 = given_time1.split(":")[0]
                            threshold_time1 = threshold_time.split(":")
                            threshold_time_2 = threshold_time.split(":")[0]
                            now = datetime.datetime.now()
                            given_time = now.replace(hour=int(given_time[0]), minute=int(given_time[1]),second=0,microsecond=0)
                            threshold_time1 = now.replace(hour=int(threshold_time[0]), minute=int(threshold_time[1]))
                            callback_time = date1+" "+time1
                            if int(given_time_1) <= int(threshold_time_2):   #Acc Time
                                print("Acc Time")
                                if int(given_time_1) >12:
                                    given_time_1 =int(given_time_1)-12
                                if date == "today" or date == "true":
                                    print("Same day,Acc time")  #---->1
                                    dispatcher.utter_template("utter_bot_call_later_time_available_"+emi_flow+"_static"+SRP+bot_gender,tracker,callback_time=int(given_time_1),customer_name=customer_name,monthly_emi=emi_amount,monthly_emi_date=due_date_resposne,housing_finance=bank_name)
                                    send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Available",flag=TIMEOUT_FLAG,emi_flow=emi_flow,callback_time = callback_time)
                                    return [FollowupAction("action_listen"), AllSlotsReset()]
                                else:
                                    print("UN DATE,Acc time")            #---->2
                                    send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Unavailable",flag=DEFAULT_FLAG,emi_flow=emi_flow,callback_time=callback_time)
                                    return [
                                        FollowupAction(callback_level2_form),
                                        SlotSet(REQUESTED_SLOT, None),
                                        SlotSet("trail_count", None),
                                        SlotSet("go_to_form_slot",None),
                                    ]
                            else:                               #UnAcc Time
                                print("Un Time")
                                if date == "today":
                                    print("Same day,UN time")   #---->3 
                                    dispatcher.utter_template("utter_time_greaterthan_sameday_threshold_"+emi_flow+"_static"+SRP+bot_gender,tracker,Threshold_time=threshold_time_1,customer_name=customer_name,monthly_emi=emi_amount,monthly_emi_date=due_date_resposne,housing_finance=bank_name)
                                    send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Unavailable",flag=TIMEOUT_FLAG,emi_flow=emi_flow,callback_time = callback_time)
                                    return [FollowupAction("action_listen"), AllSlotsReset()]
                                elif  date == "true":
                                    print("Acc date,UN time")   #---->5
                                    dispatcher.utter_template("utter_time_greaterthan_threshold_"+emi_flow+"_static"+SRP+bot_gender,tracker,Threshold_time=threshold_time_1,customer_name=customer_name,monthly_emi=emi_amount,monthly_emi_date=due_date_resposne,housing_finance=bank_name)
                                    send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Unavailable",flag=TIMEOUT_FLAG,emi_flow=emi_flow,callback_time = callback_time)
                                    return [FollowupAction("action_listen"), AllSlotsReset()]
                                else:
                                    print("UN DATE, Un time")            #---->2
                                    send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Unavailable",flag=DEFAULT_FLAG,emi_flow=emi_flow,callback_time=callback_time)
                                    return [
                                        FollowupAction(callback_level2_form),
                                        SlotSet(REQUESTED_SLOT, None),
                                        SlotSet("trail_count", None),
                                        SlotSet("go_to_form_slot",None),
                                    ]
                        else:
                            print("IN only date")
                            callback_time = date1
                            if date == "today" or date == "true":
                                print("Same day,No time")       #---->1
                                dispatcher.utter_template("utter_time_lesserthan_threshold_"+emi_flow+"_static"+SRP+bot_gender,tracker,customer_name=customer_name,monthly_emi=emi_amount,monthly_emi_date=due_date_resposne,housing_finance=bank_name)
                                send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Available",flag=TIMEOUT_FLAG,emi_flow=emi_flow,callback_time = callback_time)
                                return [FollowupAction("action_listen"), AllSlotsReset()]
                            else:
                                print("UN DATE")                #---->2
                                send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Unavailable",flag=DEFAULT_FLAG,emi_flow=emi_flow,callback_time=callback_time)
                                return [
                                        FollowupAction(callback_level2_form),
                                        SlotSet(REQUESTED_SLOT, None),
                                        SlotSet("trail_count", None),
                                        SlotSet("go_to_form_slot",None),
                                    ]
                    else:
                        print("NO Date,No Time987654")                            #---->4
                        send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Unavailable",flag=DEFAULT_FLAG,emi_flow=emi_flow)
                        return [
                                    FollowupAction(callback_level1_form),
                                    SlotSet(REQUESTED_SLOT, None),
                                    SlotSet("trail_count", None),
                                    SlotSet("go_to_form_slot",None),
                                ]
                        
            else:
                print("NO Date,No Time987654")                            #---->4
                send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,user_message=user_message,disposition_details="General - Callback - Unavailable",flag=DEFAULT_FLAG,emi_flow=emi_flow)
                return [
                            FollowupAction(callback_level1_form),
                            SlotSet(REQUESTED_SLOT, None),
                            SlotSet("trail_count", None),
                            SlotSet("go_to_form_slot",None),
                        ]

class ActionThirdParty(Action):
    def name(self):
        return "action_third_party"
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        account_name = tracker.get_slot("account_name_slot")
        script_type = tracker.get_slot("script_type_slot")
        send_and_store_disposition_details(
                tracker=tracker, 
                dispatcher=dispatcher, 
                flag=DEFAULT_FLAG,
                disposition_details="General - Third Party Contact")
        if account_name == "Ring" or account_name == "Ring Testing" and  (script_type == "short"):
            return [FollowupAction("thirdparty_level1_x2_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
        if account_name == "Axio" or account_name == "Axio Testing" or account_name == "SmartCoin" or account_name == "SmartCoin Testing" or account_name == "TVS Credit Collections Testing" or account_name == "TVS Credit Collections":
            return [FollowupAction("thirdparty_old_level1_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
        elif account_name == "Shriram Housing" or account_name == "Shriram Housing Testing":
            return [FollowupAction("thirdparty_level1_x_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
        else:
            return [FollowupAction("thirdparty_level1_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]

class ActionMultiplePayment(Action):
    def name(self):
        return "action_multiple_payment"
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        bot_gender = tracker.get_slot("bot_gender")
        customer_language = tracker.get_slot("customer_language_slot")
        SRP = SRP_value(customer_language,region)
        entities = tracker.latest_message["entities"]
        if entities:
            for entity in entities:
                if entity.get("entity", None) == "date":
                        dispatcher.utter_template("utter_multiple_payment_done_with_payment_date_"+emi_flow+"_static"+SRP+bot_gender,tracker)
                        send_and_store_disposition_details(
                            tracker=tracker,dispatcher=dispatcher,flag=TIMEOUT_FLAG,disposition_id="UCPPD",disposition_details="Dispute",)  
                        return [FollowupAction("action_listen"), AllSlotsReset()]
                else:
                    send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,flag=DEFAULT_FLAG,disposition_id="UCP",disposition_details="Dispute")
                    return [FollowupAction("validate_payment_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
        else:
            send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,flag=DEFAULT_FLAG,disposition_id="UCP",disposition_details="Dispute")
            return [FollowupAction("validate_payment_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]

class ActionWrongName(Action):
    def name(self):
        return 'action_wrong_name'
    def run(self,dispatcher,tracker,domain):
        emi_flow=tracker.get_slot("emi_flow")
        repeat_count=int(tracker.get_slot("repeat_count"))
        signal = tracker.latest_message.get("signal").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        dispatcher.utter_template("utter_deny_customer_name_"+emi_flow+"_static" + SRP+ bot_gender, tracker)
        send_and_store_disposition_details(
            tracker=tracker,
            dispatcher=dispatcher,
            flag=DEFAULT_FLAG,
            disposition_details="General - Deny - Wrong Name",
        )
        return [
                SlotSet(REQUESTED_SLOT, None),
                FollowupAction(tracker.active_form.get("name")),
                SlotSet("trail_count",1),
            ]

class ActionRepeatedUtterence(Action):
    def name(self):
        return "action_repeated_utterence"
    def run(self, dispatcher, tracker, domain):
        emi_flow = tracker.get_slot("emi_flow")
        gender = tracker.get_slot("gender_slot")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        bot_gender = tracker.get_slot("bot_gender")
        variation = tracker.get_slot("variation_slot")
        customer_language = tracker.get_slot("customer_language_slot")
        SRP = SRP_value(customer_language,region)
        print("variation",variation)
        dispatcher.utter_template(
            "utter_threshold_lessthan_2_"+emi_flow+"_static" + SRP + bot_gender,tracker
        )
        send_and_store_disposition_details(
            tracker=tracker,
            flag=TIMEOUT_FLAG,
            dispatcher=dispatcher,
            disposition_details="General - Hear Capability - Fail",
            emi_flow=emi_flow,
        )
        return [FollowupAction("action_listen"), AllSlotsReset()]

class ActionBranchAddress(Action):
    def name(self):
        return 'action_branch_address'
    def run(self,dispatcher,tracker,domain):
        emi_flow=tracker.get_slot("emi_flow")
        repeat_count=int(tracker.get_slot("repeat_count"))
        signal = tracker.latest_message.get("signal").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        gender = tracker.get_slot("gender_slot")
        bot_gender = tracker.get_slot("bot_gender")
        region = tracker.get_slot("region")
        collared = tracker.get_slot("collared")
        collared = collered_dict.get(collared)
        age = tracker.get_slot("age")
        age_category = calculate_age(age=age)
        typology = tracker.get_slot("typology")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        dispatcher.utter_template("utter_aptp_ask_payment_mode_cash_"+emi_flow+"_static" + SRP+ bot_gender, tracker)
        send_and_store_disposition_details(
            tracker=tracker,
            dispatcher=dispatcher,
            flag=DEFAULT_FLAG,
            disposition_details="",     ##dispo
        )
        return [
                SlotSet(REQUESTED_SLOT, None),
                FollowupAction(tracker.active_form.get("name")),
                SlotSet("trail_count",1),
            ]

class ActionDisputeResolutionSession(Action):
    def name(self):
        return 'action_dispute_resolution_session'
    def run(self,dispatcher,tracker,domain):
        emi_flow = tracker.get_slot("emi_flow")
        signal = tracker.latest_message.get("signal").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        entities = tracker.latest_message["entities"]
        gender = tracker.get_slot("gender_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        bot_gender = tracker.get_slot("bot_gender")
        online_session = tracker.get_slot("online_session_slot")
        intent = tracker.latest_message.get("temp_intent").get("name")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        if online_session == "yes":
            if sub_intent == "general_ask_inform" or sub_intent == "affirm":
                dispatcher.utter_template("utter_agree_to_participate_affirm_"+emi_flow+"_static"+SRP+bot_gender,tracker)
                send_and_store_disposition_details(
                    tracker=tracker,dispatcher=dispatcher,flag=TIMEOUT_FLAG,
                    disposition_id="Online Session",disposition_details="affirm")
                return [FollowupAction("action_listen"), AllSlotsReset()]
            else:
                send_and_store_disposition_details(
                    tracker=tracker,dispatcher=dispatcher,flag=DEFAULT_FLAG,
                    disposition_id="Online Session",disposition_details="deny")
                return decide_slot(tracker)
        else:
            dispatcher.utter_template(
                "utter_quantitative_data_alt_response_"+emi_flow+"_static"
                + SRP
                + bot_gender,
                tracker)
            send_and_store_disposition_details(
                    tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG,disposition_details="Online Session"
                )
            return get_return_values(tracker)

class ActionInitialMessage(Action):
    def name(self):
        return "action_initial_message"

    def run(self, dispatcher, tracker, domain):
        
        customer_deatils = get_user_details(tracker)
        print("7177customer_deatils", customer_deatils)
        emi_flow = customer_deatils["flow_type"]
        loan_id = customer_deatils["loan_id"]
        customer_name = customer_deatils["Employee Name"]
        customer_language = customer_deatils["language"]
        typology = customer_deatils["typology"]
        emi_amount = customer_deatils["EMI Amount"]
        due_date = customer_deatils["emi_date"]
        due_date_without_formatting = customer_deatils["emi_date"]
        due_date = datetime.datetime.strptime(due_date, "%d-%m-%Y")
        due_date = due_date.strftime("%d %B").lstrip('0')
        given_date = datetime.datetime.strptime(due_date_without_formatting, "%d-%m-%Y")
        no_of_days = given_date.date() - datetime.datetime.now().date()
        gender = customer_deatils["gender"]
        region = customer_deatils["region"].lower()
        region = region_dict.get(region)
        collared = customer_deatils["collared"].lower()
        age = customer_deatils["age"]
        geographic_location = customer_deatils["geographic_location"]
        tenure_left = customer_deatils["tenure_left"]
        loan_amount_remaining = customer_deatils["loan_amount_remaining"]
        loan_end_date = customer_deatils["loan_end_date"]
        loan_start_date = customer_deatils["loan_start_date"]
        principal_amount = customer_deatils["principal_amount"]
        interest_rate = customer_deatils["interest_rate"]
        total_loan_amount = customer_deatils["total_loan_amount"]
        givenTime = customer_deatils["givenTime"]
        client_name = customer_deatils["client_name"]
        bank_name = customer_deatils["bank_name"]
        agent_name = customer_deatils["agent_name"]
        supported_lang = customer_deatils["supported_languages"]
        sender_id = tracker.sender_id
        red_lang.set(str(sender_id)+"supported_languages",str(supported_lang),ex=300)
        threshold_days = customer_deatils["threshold_days"]
        pay_via_online = customer_deatils["pay_via_online"]
        pay_via_agent = customer_deatils["pay_via_agent"]
        pay_via_upi = customer_deatils["pay_via_upi"]
        pay_via_card = customer_deatils["pay_via_card"]
        pay_via_netbanking = customer_deatils["pay_via_netbanking"]
        pay_via_wallet = customer_deatils["pay_via_wallet"]
        pay_via_branch = customer_deatils["pay_via_branch"]
        pay_via_app = customer_deatils["pay_via_app"]
        late_fee_percentage = customer_deatils["late_fees"]
        threshold_time = customer_deatils["threshold_time"]
        partial_payment = customer_deatils["partial_payment"]
        level_of_negotiation  = customer_deatils["level_of_negotiation"]
        sms_integration = customer_deatils["sms_integration"]
        Partial_payment_stage = customer_deatils["Partial_payment_stage"]
        minimum_nogotiation_percentage = customer_deatils["minimum_nogotiation_percentage"]
        disposition_name  = customer_deatils["disposition_name"]
        no_of_loans = customer_deatils["no_of_loans"]
        threshold_time_1 = customer_deatils["threshold_time_1"]
        th_ptp_time = customer_deatils["th_ptp_time"]
        lender_name = customer_deatils["lender_name"]
        script_type = customer_deatils["script_type"]
        agent_desktop = customer_deatils["agent_desktop"]
        insurance = customer_deatils["insurance"]
        online_session = customer_deatils["online_session"]
        branch_name = customer_deatils["branch_name"]  
        try:  
            agent_type = customer_deatils["agent_type"]    
        except:
            agent_type = "both"
        variation = customer_deatils["variation"]
        if variation == "v1" or variation == "":
            variation = ""
        else:
            variation =  variation + "_"

        ptp_date = customer_deatils["ptp_date"]
        if ptp_date != "":
            ptp_date = datetime.datetime.strptime(ptp_date, "%d-%m-%Y")
            ptp_date = ptp_date.strftime("%d %B %Y").lstrip('0')
        else:
            ptp_date=ptp_date

        accountName = customer_deatils["accountName"]
        account_name = accountName
        accountName = accountName.replace(" Testing","").replace(" ","")
        if accountName == "ManappuramGoldLoan":
            accountName = "Manappuram"
        product = customer_deatils["product"]
        if " " in product:
            product = product.replace(" ","")
        productCategory = customer_deatils["productCategory"]
        accountName = str("_"+accountName+"_"+product+"_"+productCategory)
        if product == "":
            accountName = ""
        if accountName == "ManappuramGoldLoan_GoldLoan_General":
            accountName = "Manappuram_GoldLoan_General"

        minimum_pp_emi_amount = int(emi_amount/100*minimum_nogotiation_percentage)
        maximum_pp_emi_amount_percentage = int(minimum_nogotiation_percentage+100)/2
        maximum_pp_emi_amount = int((emi_amount/100)*maximum_pp_emi_amount_percentage)
        delay_reason_needed = "yes"
        payment_status = customer_deatils["payment_status"]
        # paid_date = customer_deatils["paid_date"]
        if ("SmartCoin"  in account_name) and emi_flow == "duedate":
            th_ptp_time = "17:00"
        # if paid_date != "":
        #     paid_date = datetime.datetime.strptime(paid_date, "%d-%m-%Y").strftime("%d %B").lstrip('0')
        loan_type = customer_deatils["loan_type"]
        auto_debit = customer_deatils["auto_debit"]
        if auto_debit == "autodebit":
            auto_debit = "auto debit"
        late_payment_policy = customer_deatils["late_payment_policy"]
        call_back_date = customer_deatils["call_back_date"]
        call_back_time = customer_deatils["call_back_time"]
        Audio_server = customer_deatils["Audio_server"]

        if emi_flow == "predue" or emi_flow.lower() == "femi" or emi_flow.lower() == "oit" or emi_flow.lower() == "OIT" or emi_flow.lower() == "non_femi":
            today1 = datetime.datetime.today().date()
            due_date1 = datetime.datetime.strptime(customer_deatils["emi_date"], "%d-%m-%Y").date()
            threshold_days = (due_date1 - today1).days
        else:
            threshold_days = threshold_days

        if emi_flow == "predue" or emi_flow == "FEMI":
            today1 = datetime.datetime.today().date()
            call_back_date = due_date
            due_date1 = datetime.datetime.strptime(customer_deatils["emi_date"], "%d-%m-%Y").date()
            call_back_days = (due_date1 - today1).days
        else:
            call_back_days = int(call_back_date)
            call_back_date = datetime.datetime.now()+timedelta(days=call_back_days)
            call_back_date = call_back_date.strftime("%d %B %Y").lstrip('0')

        if agent_type == "male":            # Male Agent only
            bot_gender_backend = "M"
        elif agent_type == "female":        # Female Agent Only
            bot_gender_backend = "F"
        else:                               # Both Agent Gender
            if gender == "F":
                bot_gender_backend = "M"
            else:
                bot_gender_backend = "F"
        
        if gender == "F":
            bot_gender = "_M"+accountName
        else:
            bot_gender = "_F"+accountName



        payment_method = []
        list_of_keys_to_skip = ["partial_payment","sms_integration","auto_debit"]
        for key in customer_deatils.keys():
            if key not in list_of_keys_to_skip:
                if customer_deatils[key] == "yes":
                    payment_method.append(key.split("_")[-1])
        pay_online_temp = copy.copy(payment_method)
        if "branch" in pay_online_temp:
            pay_online_temp.remove("branch")
        if "online" in pay_online_temp:
            pay_online_temp.remove("online")
        if "agent" in pay_online_temp:
            pay_online_temp.remove("agent")
        payment_method = ",".join(payment_method)
        pay_online_temp = ",".join(pay_online_temp)
        print("***** payment method 2",payment_method)
        print("*****he value of pay online *****",pay_online_temp)
        print("The flow type", emi_flow)
        print("The partial payment value",partial_payment)


        if int(no_of_loans) >1:
            loans = "ML"
        else:
            loans = "SL"
        loanType = "WLT"
        

        print("The flow",emi_flow)
        if  emi_flow == "predue" or emi_flow == "FEMI" or emi_flow == "duedate" or ("dpd_" in emi_flow) or emi_flow == "NPA" or emi_flow == "NOC" or emi_flow == "noc" or emi_flow == "OIT" or emi_flow == "live_penal" or emi_flow == "legal_notice" or emi_flow == "penalty_waiver" or emi_flow == "pre_npa" or emi_flow == "oit" or emi_flow == "non_femi" or emi_flow == "npa" or emi_flow == "ptp_reminder" or emi_flow == "ptp_confirmation" or emi_flow == "broken_ptp" or emi_flow == "app_activation" or emi_flow == "ftd" or emi_flow == "bureau_report" or emi_flow == "interest_discount":
            if emi_flow == "FEMI":
                emi_flow = "FEMI_unpaid"
            loan_category = loans + "_" + loanType+"_"
            if loan_category == "SL_WLT_":
                loan_category = ""
            if auto_debit ==  "auto debit":      
                loan_category = "NACH_"+loan_category
            partial_payment_count = "not_triggered"

            form_to_activate = "rpc_v1_form"
            if "paytm" in accountName.lower(): # specific to paytm
                delay_reason_needed = "no"
            return [
                FollowupAction(form_to_activate),
                SlotSet("emi_flow", str(emi_flow)),
                SlotSet("partial_payment_count",str(partial_payment_count)),
                SlotSet("loan_id", str(loan_id)),
                SlotSet("customer_name", str(customer_name)),
                SlotSet("emi_amount_slot", str(emi_amount)),
                SlotSet("due_date", str(due_date)),
                SlotSet("region", str(region)),
                SlotSet("branch_name", str(branch_name)),
                SlotSet("collared", str(collared)),
                SlotSet("age", str(age)),
                SlotSet("client_name_slot", str(client_name)),
                SlotSet("bank_name_slot",str(bank_name)),
                SlotSet("agent_name", str(agent_name)),
                SlotSet("typology", str(typology)),
                SlotSet("geographic_location", str(geographic_location)),
                SlotSet("tenure_left", str(tenure_left)),
                SlotSet("loan_amount_remaining_slot", str(loan_amount_remaining)),
                SlotSet("loan_end_date_slot", str(loan_end_date)),
                SlotSet("loan_start_date_slot", str(loan_start_date)),
                SlotSet("principal_amount_slot", str(principal_amount)),
                SlotSet("interest_rate_slot", str(interest_rate)),
                SlotSet("givenTime", str(givenTime)),
                SlotSet("total_loan_amount_slot", str(total_loan_amount)),
                SlotSet("gender_slot", str(gender)),
                SlotSet("supported_languages", str(supported_lang)),
                SlotSet("payment_method_slot", str(payment_method)),
                SlotSet("bot_gender", str(bot_gender)),
                SlotSet("bot_gender_backend", str(bot_gender_backend)),
                SlotSet("threshold_days_slot", str(threshold_days)),
                SlotSet("pay_via_online_slot", str(pay_via_online)),
                SlotSet("pay_via_agent_slot", str(pay_via_agent)),
                SlotSet("pay_via_upi_slot", str(pay_via_upi)),
                SlotSet("pay_via_card_slot", str(pay_via_card)),
                SlotSet("pay_via_net_banking_slot", str(pay_via_netbanking)),
                SlotSet("pay_via_wallet_slot", str(pay_via_wallet)),
                SlotSet("pay_via_branch_slot", str(pay_via_branch)),
                SlotSet("pay_via_app_slot", str(pay_via_app)),
                SlotSet("late_fee_percentage_slot", str(late_fee_percentage)),
                SlotSet("pay_online_slot", str(pay_online_temp)),
                SlotSet("customer_language_slot", str(customer_language)),
                SlotSet("due_date_without_formatting_slot", str(due_date_without_formatting)),
                SlotSet("threshold_time_slot",str(threshold_time)),
                SlotSet("partial_payment_slot",str(partial_payment)),
                SlotSet("level_of_negotiation_slot",str(level_of_negotiation)),
                SlotSet("sms_integration_slot",str(sms_integration)),
                SlotSet("Partial_payment_stage_slot",str(Partial_payment_stage)),
                SlotSet("minimum_nogotiation_percentage_slot",str(minimum_nogotiation_percentage)),
                SlotSet("minimum_pp_emi_amount_slot",str(minimum_pp_emi_amount)),
                SlotSet("maximum_pp_emi_amount_slot",str(maximum_pp_emi_amount)),
                SlotSet("disposition_name_slot",str(disposition_name)),
                SlotSet("no_of_days_slot",abs(no_of_days.days)),
                SlotSet("Audio_server_slot",Audio_server),
                SlotSet("payment_status_slot",payment_status),
                # SlotSet("paid_date_slot",paid_date),
                SlotSet("loan_type_slot",str(loan_type)),
                SlotSet("no_of_loans_slot",str(no_of_loans)),
                SlotSet("auto_debit_slot",str(auto_debit)),
                SlotSet("loan_category_slot",str(loan_category)),
                SlotSet("late_payment_policy_slot",str(late_payment_policy)),
                SlotSet("call_back_date_slot",str(call_back_date)),
                SlotSet("call_back_time_slot",str(call_back_time)),
                SlotSet("call_back_time_slot_1",str(threshold_time_1)),
                SlotSet("call_back_days_slot",str(call_back_days)),
                SlotSet("ptp_date_slot",str(ptp_date)),
                SlotSet("variation_slot",str(variation)),
                SlotSet("account_name_slot",str(account_name)),
                SlotSet("delay_reason_needed_slot",str(delay_reason_needed)),
                SlotSet("th_ptp_time_slot",str(th_ptp_time)),
                SlotSet("lender_name_slot",str(lender_name)),
                SlotSet("script_type_slot",str(script_type)),
                SlotSet("agent_desktop_slot",str(agent_desktop)),
                SlotSet("insurance_slot",str(insurance)),
                SlotSet("online_session_slot",str(online_session)),
            ]

        elif emi_flow == "ivr":
            if emi_flow == "FEMI":
                emi_flow = "FEMI_unpaid"
            loan_category = loans + "_" + loanType+"_"
            if loan_category == "SL_WLT_":
                loan_category = ""
            if auto_debit ==  "auto debit":      
                loan_category = "NACH_"+loan_category
            partial_payment_count = "not_triggered"

            form_to_activate = "ivr_blast_form"
            return [
                FollowupAction(form_to_activate),
                SlotSet("emi_flow", str(emi_flow)),
                SlotSet("partial_payment_count",str(partial_payment_count)),
                SlotSet("loan_id", str(loan_id)),
                SlotSet("customer_name", str(customer_name)),
                SlotSet("emi_amount_slot", str(emi_amount)),
                SlotSet("due_date", str(due_date)),
                SlotSet("region", str(region)),
                SlotSet("branch_name", str(branch_name)),
                SlotSet("collared", str(collared)),
                SlotSet("age", str(age)),
                SlotSet("client_name_slot", str(client_name)),
                SlotSet("bank_name_slot",str(bank_name)),
                SlotSet("agent_name", str(agent_name)),
                SlotSet("typology", str(typology)),
                SlotSet("geographic_location", str(geographic_location)),
                SlotSet("tenure_left", str(tenure_left)),
                SlotSet("loan_amount_remaining_slot", str(loan_amount_remaining)),
                SlotSet("loan_end_date_slot", str(loan_end_date)),
                SlotSet("loan_start_date_slot", str(loan_start_date)),
                SlotSet("principal_amount_slot", str(principal_amount)),
                SlotSet("interest_rate_slot", str(interest_rate)),
                SlotSet("total_loan_amount_slot", str(total_loan_amount)),
                SlotSet("gender_slot", str(gender)),
                SlotSet("supported_languages", str(supported_lang)),
                SlotSet("payment_method_slot", str(payment_method)),
                SlotSet("bot_gender", str(bot_gender)),
                SlotSet("threshold_days_slot", str(threshold_days)),
                SlotSet("pay_via_online_slot", str(pay_via_online)),
                SlotSet("pay_via_agent_slot", str(pay_via_agent)),
                SlotSet("pay_via_upi_slot", str(pay_via_upi)),
                SlotSet("pay_via_card_slot", str(pay_via_card)),
                SlotSet("pay_via_net_banking_slot", str(pay_via_netbanking)),
                SlotSet("pay_via_wallet_slot", str(pay_via_wallet)),
                SlotSet("pay_via_branch_slot", str(pay_via_branch)),
                SlotSet("pay_via_app_slot", str(pay_via_app)),
                SlotSet("late_fee_percentage_slot", str(late_fee_percentage)),
                SlotSet("pay_online_slot", str(pay_online_temp)),
                SlotSet("customer_language_slot", str(customer_language)),
                SlotSet("due_date_without_formatting_slot", str(due_date_without_formatting)),
                SlotSet("threshold_time_slot",str(threshold_time)),
                SlotSet("partial_payment_slot",str(partial_payment)),
                SlotSet("level_of_negotiation_slot",str(level_of_negotiation)),
                SlotSet("sms_integration_slot",str(sms_integration)),
                SlotSet("Partial_payment_stage_slot",str(Partial_payment_stage)),
                SlotSet("minimum_nogotiation_percentage_slot",str(minimum_nogotiation_percentage)),
                SlotSet("minimum_pp_emi_amount_slot",str(minimum_pp_emi_amount)),
                SlotSet("maximum_pp_emi_amount_slot",str(maximum_pp_emi_amount)),
                SlotSet("disposition_name_slot",str(disposition_name)),
                SlotSet("no_of_days_slot",abs(no_of_days.days)),
                SlotSet("Audio_server_slot",Audio_server),
                SlotSet("payment_status_slot",payment_status),
                SlotSet("paid_date_slot",paid_date),
                SlotSet("loan_type_slot",str(loan_type)),
                SlotSet("no_of_loans_slot",str(no_of_loans)),
                SlotSet("auto_debit_slot",str(auto_debit)),
                SlotSet("loan_category_slot",str(loan_category)),
                SlotSet("late_payment_policy_slot",str(late_payment_policy)),
                SlotSet("call_back_date_slot",str(call_back_date)),
                SlotSet("call_back_time_slot",str(call_back_time)),
                SlotSet("call_back_time_slot_1",str(threshold_time_1)),
                SlotSet("call_back_days_slot",str(call_back_days)),
                SlotSet("ptp_date_slot",str(ptp_date)),
                SlotSet("variation_slot",str(variation)),
                SlotSet("account_name_slot",str(account_name)),
                SlotSet("delay_reason_needed_slot",str(delay_reason_needed)),
                SlotSet("th_ptp_time_slot",str(th_ptp_time)),
                SlotSet("lender_name_slot",str(lender_name)),
                SlotSet("script_type_slot",str(script_type)),
                SlotSet("agent_desktop_slot",str(agent_desktop)),
                SlotSet("insurance_slot",str(insurance)),
                SlotSet("online_session_slot",str(online_session)),
            ]
        
        else:
            send_and_store_disposition_details(
                    tracker=tracker,
                    dispatcher=dispatcher,
                    flag=TIMEOUT_FLAG,
                    disposition_details="Wrong Flow Name",  ## should not be shown in pravid
                    emi_flow=emi_flow,
                )
            return [FollowupAction("action_listen"), AllSlotsReset()]
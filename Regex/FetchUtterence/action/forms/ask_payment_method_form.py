from datetime import timedelta
import datetime
from re import template
import time
from actions.utils.common_imports import *
from actions.utils.helper import *
helper = Helper()


class AskPaymentMethod(FormAction):
    def name(self):  # type: () -> Text
        return "ask_payment_method_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        stop_conversation = tracker.get_slot("stop_conversation")
        ask_payment_method = tracker.get_slot("ask_payment_method")
        if stop_conversation == "TRUE":
            return []
        return ["ask_payment_method"]


    def slot_mappings(self):  # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        return {
            "ask_payment_method": [
                self.from_intent(intent="ask", value="TRUE"),
                self.from_intent(intent="inform", value="TRUE"),
                self.from_intent(intent="pay_via_net_banking", value="pay_via"),
                self.from_intent(intent="pay_via_agent", value="pay_via"),
                self.from_intent(intent="pay_via_app", value="pay_via"),
                self.from_intent(intent="pay_via_card", value="pay_via"),
                self.from_intent(intent="pay_via_wallet", value="pay_via"),
                self.from_intent(intent="pay_via_branch", value="pay_via"),
                self.from_intent(intent="pay_via_online", value="pay_via"),
                self.from_intent(intent="pay_via_upi", value="pay_via"),
            ],
        }

    @staticmethod
    def _should_request_slot(tracker, slot_name):  # type: (Tracker, Text) -> bool
        """Check whether form action should request given slot"""
        return tracker.get_slot(slot_name) is None

    def request_next_slot(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ):
        for slot in self.required_slots(tracker):
            trail_count = tracker.get_slot("trail_count")
            if self._should_request_slot(tracker, slot):
                emi_amount = tracker.get_slot("emi_amount_slot")
                emi_flow = tracker.get_slot("emi_flow")
                age = tracker.get_slot("age")
                region = tracker.get_slot("region")
                collared = tracker.get_slot("collared")
                client_name = tracker.get_slot("client_name_slot")
                bank_name = tracker.get_slot("bank_name_slot")
                agent_name = tracker.get_slot("agent_name")
                gender = tracker.get_slot("gender_slot")
                age_category = calculate_age(age)
                collared = collered_dict.get(collared)
                typology = tracker.get_slot("typology")
                customer_language = tracker.get_slot("customer_language_slot")
                SRP = SRP_value(customer_language,region)
                print("The value of SRP",SRP)
                disposition_name = tracker.get_slot("disposition_name_slot")
                SRP = SRP_value(customer_language,region)
                bot_gender = tracker.get_slot("bot_gender")
                current_main_slot = tracker.get_slot("current_main_slot")
                nlu_data_list = tracker.get_slot("nlu_data_list_slot")
                print("the typolofy category", typology)
                print("emiamount",emi_amount)
                print("the region category", region)
                print("the age category", age_category)
                print("the collared category", collared)
                print("the gender ", gender)
                print("the disposition_name ", disposition_name)
                print("311In_slot",slot)
                try:
                    signal = tracker.latest_message.get("signal").get("name")
                except:
                    signal = tracker.latest_message.get("intent").get("name")
                nlu_data_list,count = repeat_verifier(nlu_data_list,slot+"-"+signal)
                print("mpe_nlu_data_list",nlu_data_list)
                if count:
                    return [FollowupAction("action_repeated_utterence"),SlotSet("nlu_data_list_slot", nlu_data_list),]
                if slot == "ask_payment_method":
                    if trail_count is None:
                        trail_count = 0
                        template_name = (
                            "utter_aptp_ask_payment_mode_"+emi_flow+"_static"+SRP+bot_gender
                        )
                        dispatcher.utter_template(template_name, tracker)
                    else:
                        template_name = (
                           "utter_aptp_ask_payment_mode_trim_"+emi_flow+"_static"+SRP+bot_gender
                        )
                        dispatcher.utter_template(template_name, tracker)
                    send_and_store_disposition_details(
                    tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG,disposition_id=""
                )
                return [
                    FollowupAction("action_listen"),
                    SlotSet(REQUESTED_SLOT, slot),
                    SlotSet("timestamp", time.time()),
                    SlotSet("trail_count", trail_count + 1),
                    SlotSet("current_main_slot",current_main_slot),
                    SlotSet("nlu_data_list_slot", nlu_data_list),
                ]

    

    @staticmethod
    def validate_ask_payment_method(
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ):
        
        print("entering into ask_payment_method slot")
        intent = tracker.latest_message.get("intent").get("name")
        sub_intent = tracker.latest_message.get("sub_intent").get("name")
        Humiliate = tracker.latest_message.get("Humiliate").get("name")
        sub_context = tracker.latest_message.get("sub_context").get("name")
        delay_reason = tracker.latest_message.get("delay_reason").get("name")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        context = tracker.latest_message.get("context").get("name")
        third_person = tracker.latest_message.get("third_person").get("name")
        signal = tracker.latest_message.get("signal").get("name")
        gender = tracker.get_slot("gender_slot")
        threshold_days = tracker.get_slot("threshold_days_slot")
        entities = tracker.latest_message["entities"]
        payment_method = paymentMode(tracker,"available_payment_mode")
        customer_language = tracker.get_slot("customer_language_slot")
        region = tracker.get_slot("region")
        SRP = SRP_value(customer_language,region)
        auto_debit = tracker.get_slot("auto_debit_slot")
        auto_debit_nach = auto_debit_Nach(auto_debit)
        auto_debit_onlynach = auto_debit_onlyNach(auto_debit)
        emi_flow = tracker.get_slot("emi_flow")
        partial_payment = tracker.get_slot("partial_payment_slot")
        partial_payment_stage_slot = tracker.get_slot("Partial_payment_stage_slot")
        move_to_new_slot = tracker.get_slot("move_to_new_slot")
        disposition_name = tracker.get_slot("disposition_name_slot")
        due_date = tracker.get_slot("due_date_without_formatting_slot")
        emi_amount = tracker.get_slot("emi_amount_slot")
        level_of_negotiation = tracker.get_slot("level_of_negotiation_slot")
        partial_payment_count = tracker.get_slot("partial_payment_count")
        minimum_pp_emi_amount = tracker.get_slot("minimum_pp_emi_amount_slot")
        maximum_pp_emi_amount = tracker.get_slot("maximum_pp_emi_amount_slot")
        loan_category = tracker.get_slot("loan_category_slot")
        user_message = tracker.latest_message.get("text")
        threshold_time = tracker.get_slot("threshold_time_slot")
        threshold_time_1 = tracker.get_slot("call_back_time_slot_1")
        sentiment = tracker.latest_message.get("sentiment").get("name")
        print("threshold_time_121212",threshold_time_1)
        SRP = SRP_value(customer_language,region)
        current_main_slot = tracker.get_slot("current_main_slot")
        bot_gender = tracker.get_slot("bot_gender")
        auto_payment = tracker.get_slot("auto_payment_slot")
        call_back_days = tracker.get_slot("call_back_days_slot")
        due_date_resposne = tracker.get_slot("due_date")
        bank_name = tracker.get_slot("bank_name_slot")
        customer_name = tracker.get_slot("customer_name")
        print("The value of threshold_days,", threshold_days)
        print("295The payment_methods are",payment_method)
        print(
            Humiliate,
            sub_context,
            delay_reason,
            sentiment,
            context,
            third_person,
            signal,
            sub_intent,
            gender)
        if value == "pay_via":
            print("here pay_via")
            temp_intent =tracker.latest_message.get("temp_intent").get("name")
            user_payment_mode_eligible = tracker.get_slot(signal+"_slot")
            print("user_payment_mode_eligible12",user_payment_mode_eligible)
            user_payment_mode = signal.split("pay_via_")[-1].replace("_"," ")
            print("user_payment_mode123",user_payment_mode)
            dispo_payment = {
                "pay_via_net_banking":" Netbanking - APTP",
                "pay_via_agent":" Agent Payment - APTP",
                "pay_via_app":" App Payment - APTP",
                "pay_via_card":" Card Payment - APTP",
                "pay_via_wallet":" Wallet Payment - APTP",
                "pay_via_branch":" Branch Payment - APTP",
                "pay_via_online":" Online Payment - APTP",
                "pay_via_upi":" UPI Payment - APTP",
            }
            if user_payment_mode_eligible == "yes":
                if temp_intent == "ask" and context == "payment":
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
                    dispatcher.utter_template(
                        template_name, tracker, tracker, available_payment_mode=payment_method
                    )
                    send_and_store_disposition_details(
                        tracker=tracker,
                        flag=DEFAULT_FLAG,
                        dispatcher=dispatcher,
                        disposition_details=temp_intent.capitalize()+" Payment Method")
                    return {"ask_payment_method":None,"trail_count":1}
                else:
                    dispatcher.utter_template("utter_acceptable_payment_mode_noPTP_"+emi_flow+"_static"+SRP+bot_gender,tracker,user_requested_payment_option=user_payment_mode)
                    send_and_store_disposition_details(
                        tracker=tracker,dispatcher=dispatcher,flag=TIMEOUT_FLAG,disposition_details=temp_intent.capitalize()+dispo_payment[signal],)
                    return {"ask_payment_method": value,"stop_conversation": "TRUE",}
            else:
                dispatcher.utter_template("utter_non_acceptable_payment_mode_noPTP_"+emi_flow+"_static"+SRP+bot_gender,tracker)
                send_and_store_disposition_details(
                    tracker=tracker,dispatcher=dispatcher,flag=TIMEOUT_FLAG,disposition_details=temp_intent.capitalize()+dispo_payment[signal],)  ##dispo
                return {"ask_payment_method": value,"stop_conversation": "TRUE",}
        if value == "TRUE":
            if signal == "make_payment" and sub_intent == "deny":
                send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,flag=DEFAULT_FLAG,disposition_id="RTP")
                return {"ask_payment_method": None,"go_to_form_slot":"dtp","stop_conversation": "TRUE"}
            if (
                    signal == "make_payment"
                    and delay_reason == "no_delay_reason"
                    and context == "payment"
                    and sub_context == "process" 
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
                    dispatcher.utter_template(
                        template_name, tracker, tracker, available_payment_mode=payment_method
                    )
                    send_and_store_disposition_details(
                        tracker=tracker,
                        flag=DEFAULT_FLAG,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Payment Method")
                    return {"ask_payment_method":None,"trail_count":1}
            else:
                dispatcher.utter_template("utter_non_acceptable_payment_mode_noPTP_"+emi_flow+"_static"+SRP+bot_gender,tracker)
                send_and_store_disposition_details(
                    tracker=tracker,dispatcher=dispatcher,flag=TIMEOUT_FLAG,disposition_id="ATP")  ##dispo
                return {"ask_payment_method": value,"stop_conversation": "TRUE",}
        return {"ask_payment_method": None}

            
    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        
        go_to_form = tracker.get_slot("go_to_form_slot")
        flow_data = tracker.get_slot("flow_data_slot")
        emi_flow = tracker.get_slot("emi_flow")
        account_name = tracker.get_slot("account_name_slot")
        if go_to_form == "dtp":
            return decide_slot(tracker)
        return [FollowupAction("action_listen"), AllSlotsReset()]

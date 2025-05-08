from datetime import timedelta
import datetime
from re import template
import time
from actions.utils.common_imports import *
from actions.utils.helper import *
helper = Helper()


class AskFollowUP(FormAction):
    def name(self):  # type: () -> Text
        return "ask_follow_up_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        stop_conversation = tracker.get_slot("stop_conversation")
        ask_followup_question = tracker.get_slot("ask_followup_question")
        if stop_conversation == "TRUE":
            return []
        return ["ask_followup_question"]


    def slot_mappings(self):  # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        return {
            "ask_followup_question":[
                self.from_intent(intent="affirm", value="TRUE"),
                self.from_intent(intent="ask", value="TRUE"),
                self.from_intent(intent="inform", value="TRUE"),
                self.from_intent(intent="deny", value="FALSE"),
                self.from_intent(intent="third_party_contact", value="FALSE"),
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
                customer_name = tracker.get_slot("customer_name")
                due_date = tracker.get_slot("due_date")
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
                move_to_new_slot = tracker.get_slot("move_to_new_slot")
                supported_languages_1 = tracker.get_slot("supported_languages")
                ask_delay_reason_count = tracker.get_slot("ask_delay_reason_count")
                came_from_disposition_slot = tracker.get_slot("came_from_disposition_slot")
                no_of_days_slot = tracker.get_slot("no_of_days_slot")
                threshold_time = tracker.get_slot("threshold_time_slot")
                loan_category = tracker.get_slot("loan_category_slot")
                auto_debit = tracker.get_slot("auto_debit_slot")
                paid_date = tracker.get_slot("paid_date_slot")
                loan_type = tracker.get_slot("loan_type_slot")
                no_of_loans = tracker.get_slot("no_of_loans_slot")
                emi_slot_temp = tracker.get_slot("emi_slot_temp_slot")
                SRP = SRP_value(customer_language,region)
                bot_gender = tracker.get_slot("bot_gender")
                call_back_date = tracker.get_slot("call_back_date_slot")
                current_main_slot = tracker.get_slot("current_main_slot")
                nlu_data_list = tracker.get_slot("nlu_data_list_slot")
                ptp_date = tracker.get_slot("ptp_date_slot")
                auto_payment = tracker.get_slot("auto_payment_slot")
                variation = tracker.get_slot("variation_slot")

                print("the typolofy category", typology)
                print("emiamount",emi_amount)
                print("the region category", region)
                print("the age category", age_category)
                print("the collared category", collared)
                print("the gender ", gender)
                print("the disposition_name ", disposition_name)
                print("311In_slot",slot)
                print("311In_slot",slot)
                try:
                    signal = tracker.latest_message.get("signal").get("name")
                except:
                    signal = tracker.latest_message.get("intent").get("name")
                nlu_data_list,count = repeat_verifier(nlu_data_list,slot+"-"+signal)
                print("mpe_nlu_data_list",nlu_data_list)
                if count:
                    print("repeeet")
                    return [FollowupAction("action_repeated_utterence"),SlotSet("nlu_data_list_slot", nlu_data_list),]
                if auto_debit == "auto debit":             
                    temp_auto_debit = "NACH_"                         ##verfi      NON_NACH
                else:
                    temp_auto_debit = ""

                if slot == "ask_followup_question":
                    if trail_count is None:
                        trail_count = 0
                        dispatcher.utter_template("utter_follow_up_for_health_issue_affirm_"+variation+loan_category+emi_flow+"_static"+SRP+bot_gender, tracker,monthly_emi = emi_amount,monthly_emi_date = due_date)
                        send_and_store_disposition_details(tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG,disposition_id="PDR")
                    else:
                        dispatcher.utter_template("utter_follow_up_for_health_issue_affirm_"+variation+loan_category+emi_flow+"_static"+SRP+bot_gender, tracker,monthly_emi = emi_amount,monthly_emi_date = due_date)
                        send_and_store_disposition_details(tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG)
                return [
                    FollowupAction("action_listen"),
                    SlotSet(REQUESTED_SLOT, slot),
                    SlotSet("timestamp", time.time()),
                    SlotSet("trail_count", trail_count + 1),
                    SlotSet("ask_delay_reason_count",ask_delay_reason_count+1),
                    SlotSet("current_main_slot",current_main_slot),
                    SlotSet("nlu_data_list_slot", nlu_data_list),
                ]

    @staticmethod
    def validate_ask_followup_question(
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ):
        if value == "TRUE":
            print("entering into form")
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
            payment_method = paymentMode(tracker,"available_payment_mode")
            customer_language = tracker.get_slot("customer_language_slot")
            region = tracker.get_slot("region")
            SRP = SRP_value(customer_language,region)
            auto_debit = tracker.get_slot("auto_debit_slot")
            auto_debit_nach = auto_debit_Nach(auto_debit)
            auto_debit_onlynach = auto_debit_onlyNach(auto_debit)
            emi_flow = tracker.get_slot("emi_flow")
            partial_payment = tracker.get_slot("partial_payment_slot")
            threshold_days = tracker.get_slot("threshold_days_slot")
            partial_payment_stage_slot = tracker.get_slot("Partial_payment_stage_slot")
            move_to_new_slot = tracker.get_slot("move_to_new_slot")
            loan_category = tracker.get_slot("loan_category_slot")
            SRP = SRP_value(customer_language,region)
            bot_gender = tracker.get_slot("bot_gender")
            customer_name = tracker.get_slot("customer_name")
            due_date_resposne = tracker.get_slot("due_date")
            emi_amount = tracker.get_slot("emi_amount_slot")
            bank_name = tracker.get_slot("bank_name_slot")
            entities = tracker.latest_message["entities"]
            
            if signal == "deny":
                send_and_store_disposition_details(
                                    tracker=tracker,dispatcher=dispatcher,flag=DEFAULT_FLAG,)
                return {"ask_followup_question":None,"go_to_form_slot":"deny","trail_count":None,"stop_conversation":True}
            if signal == "donot_want_to_pay":
                send_and_store_disposition_details(
                    tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG,disposition_id="RTP")
                return {"ask_followup_question":None,"go_to_form_slot":"deny", "trail_count": None,"stop_conversation": "TRUE"}
            if (signal == "general_chat" and sub_intent == "deny"):
                if partial_payment == "yes" and partial_payment_stage_slot == "stage1":
                    send_and_store_disposition_details(tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG,)
                    print("move to pp from slot1 Frst")
                    return {"ask_followup_question":value,"back_to_partial_payment":"yes","changing_slot":"ask_followup_question","partial_payment_count":"not_triggered","came_from_delay_reason":"False"}
                else:
                    send_and_store_disposition_details(
                                    tracker=tracker,
                                    flag=DEFAULT_FLAG,
                                    dispatcher=dispatcher,disposition_id="RTP")
                    return {"ask_followup_question": None,"go_to_form_slot":"deny", "trail_count": None,"stop_conversation": "TRUE"}
            if (
                signal == "general_chat"
                and sub_context == "general" or sub_context == "action_by_customer"
                and sub_intent == "general_ask_inform" or sub_intent == "affirm"
                and context == "general"
            ):
                if move_to_new_slot == "TRUE":
                    send_and_store_disposition_details(tracker=tracker,dispatcher=dispatcher,flag=DEFAULT_FLAG)
                    return {"ask_followup_question":"ask_followup_question","trail_count":None}
                else:
                    if entities:
                        for entity in entities:
                            if entity.get("entity", None) == "date":
                                if entity.get("entity", None) == "date":
                                    given_date = datetime.datetime.strptime(
                                        entity["value"], "%d/%m/%Y"
                                    )
                                    print("given date", given_date)
                                    no_of_days = (
                                        given_date.date() - datetime.datetime.now().date()
                                    )
                                    print("no_of_days", no_of_days.days)
                                    if no_of_days.days <= int(threshold_days):
                                        send_and_store_disposition_details(
                                            tracker=tracker,
                                            dispatcher=dispatcher,
                                            flag=DEFAULT_FLAG,
                                        )
                                        return {
                                            "ask_followup_question": None,"go_to_form_slot":"aptp",
                                            "stop_conversation": "TRUE",
                                        }
                                    else:
                                        send_and_store_disposition_details(
                                            tracker=tracker,
                                            dispatcher=dispatcher,
                                            flag=DEFAULT_FLAG,
                                        )
                                        dispatcher.utter_template("utter_affirm_nonAccPTP_positive_"+emi_flow+"_static"
                                        + SRP
                                        + bot_gender,
                                        tracker)
                                        return {
                                            "ask_followup_question": None,"go_to_form_slot":"deny",
                                            "trail_count": None,"stop_conversation": "TRUE"
                                        }
                    else:
                        send_and_store_disposition_details(
                            tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG
                        )
                        return {
                            "ask_followup_question": None,"go_to_form_slot":"payment_re_confirmation",
                            "trail_count": None,"stop_conversation": "TRUE"
                        }
            
            if (
                signal == "make_payment" and sub_intent == "deny" and sub_context == "general"):
                send_and_store_disposition_details(tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG)
                if partial_payment == "yes" and partial_payment_stage_slot == "stage1":
                    print("move to pp from slot1 second")
                    return {"back_to_partial_payment":"yes"}
                else:
                    send_and_store_disposition_details(
                        tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG)
                    return {"ask_followup_question": None,"go_to_form_slot":"deny", "trail_count": None,"stop_conversation": "TRUE"}
            if (
                signal == "general_chat"
                and sub_context == "general"
                or sub_context == "action_by_customer"
                and sub_intent == "affirm"
                and context == "general"
            ):
                if entities:
                    for entity in entities:
                        if entity.get("entity", None) == "date":
                            if entity.get("entity", None) == "date":
                                given_date = datetime.datetime.strptime(
                                    entity["value"], "%d/%m/%Y"
                                )
                                print("given date", given_date)
                                no_of_days = (
                                    given_date.date() - datetime.datetime.now().date()
                                )
                                print("no_of_days", no_of_days.days)
                                if no_of_days.days <= int(threshold_days):
                                    send_and_store_disposition_details(
                                        tracker=tracker,
                                        dispatcher=dispatcher,
                                        flag=DEFAULT_FLAG,
                                    )
                                    return {
                                        "ask_followup_question": None,"go_to_form_slot":"aptp",
                                        "stop_conversation": "TRUE",
                                    }
                                else:
                                    send_and_store_disposition_details(
                                        tracker=tracker,
                                        dispatcher=dispatcher,
                                        flag=DEFAULT_FLAG,
                                    )
                                    dispatcher.utter_template("utter_affirm_nonAccPTP_positive_"+emi_flow+"_static"
                                    + SRP
                                    + bot_gender,
                                    tracker)
                                    return {
                                        "ask_followup_question": None,"go_to_form_slot":"deny",
                                        "trail_count": None,"stop_conversation": "TRUE"
                                    }
                else:
                    send_and_store_disposition_details(
                        tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG
                    )
                    return {
                        "ask_followup_question": None,
                        "trail_count": None,
                    }
            if (
                signal == "make_payment"
                and sub_context == "action_by_customer"
                and context == "payment"
            ):
                if entities:
                    for entity in entities:
                        if entity.get("entity", None) == "date":
                            given_date = datetime.datetime.strptime(
                                entity["value"], "%d/%m/%Y"
                            )
                            print("given date", given_date)
                            no_of_days = (
                                given_date.date() - datetime.datetime.now().date()
                            )
                            print("no_of_days", no_of_days.days)
                            if no_of_days.days <= int(threshold_days):
                                send_and_store_disposition_details(
                                    tracker=tracker,
                                    dispatcher=dispatcher,
                                    flag=DEFAULT_FLAG,
                                )
                                return {
                                    "ask_followup_question": None,"go_to_form_slot":"aptp",
                                    "stop_conversation": "TRUE",
                                }
                            else:
                                send_and_store_disposition_details(
                                    tracker=tracker,
                                    dispatcher=dispatcher,
                                    flag=DEFAULT_FLAG,
                                )
                                dispatcher.utter_template("utter_affirm_nonAccPTP_positive_"+emi_flow+"_static"
                                    + SRP
                                    + bot_gender,
                                    tracker)
                                return {
                                    "ask_followup_question": None,"go_to_form_slot":"deny",
                                    "trail_count": None,"stop_conversation": "TRUE"
                                }
                else:
                    send_and_store_disposition_details(
                        tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG
                    )
                    return {
                        "ask_followup_question": None,"go_to_form_slot":"payment_re_confirmation",
                        "trail_count": None,"stop_conversation": "TRUE"
                    }
            if (
            signal == "make_payment"
            and delay_reason == "no_delay_reason"
            and context == "payment"
            and sub_context == "process" 
            ):
                print("/////////////", payment_method,"///////////////////")
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
                    )
                print("The generated template name", template_name)
                dispatcher.utter_template(
                    template_name, tracker, tracker, available_payment_mode=payment_method
                )
                if len(entities) == 0:
                    send_and_store_disposition_details(
                        tracker=tracker,
                        flag=DEFAULT_FLAG,
                        dispatcher=dispatcher,
                        disposition_details=intent.capitalize()+" Payment Method")
                    print("Entering into NoPTP")
                    return {"ask_followup_question":None,"name_confirmation":"TRUE"}
                else:
                    for entity in entities:
                        if entity.get("entity", None) == "date":
                            given_date = datetime.datetime.strptime(
                                entity["value"], "%d/%m/%Y")
                            print("given date", given_date)
                            no_of_days = given_date.date() - datetime.datetime.now().date()
                            print("no_of_days", no_of_days.days)
                            if no_of_days.days <= int(threshold_days):
                                print("Entering into AccPTP")
                                send_and_store_disposition_details(
                                    tracker=tracker,
                                    dispatcher=dispatcher,
                                    disposition_details=intent.capitalize()+" Payment Method",
                                    disposition_id="APTP",
                                    ptp_date=given_date,
                                    flag=DEFAULT_FLAG,
                                )
                                return {
                                    "ask_followup_question": None,"go_to_form_slot":"aptp",
                                    "stop_conversation": "TRUE",
                                }
                            else:
                                
                                send_and_store_disposition_details(
                                    tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG,disposition_details=intent.capitalize()+" Payment Method",disposition_id="UPTP")
                                return {"ask_followup_question":None,"go_to_form_slot":"deny","trail_count":None,"stop_conversation": "TRUE"}
                        else:
                            send_and_store_disposition_details(
                                tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG,disposition_details=intent.capitalize()+" Payment Method")
                            return {"ask_followup_question":None,"name_confirmation":"TRUE"}

            if signal == "make_payment" and sub_intent == "affirm":
                send_and_store_disposition_details(
                    tracker=tracker, dispatcher=dispatcher, flag=DEFAULT_FLAG,disposition_id="ATP"
                )
                return {"ask_followup_question": None,"go_to_form_slot":"payment_re_confirmation","trail_count":1,"stop_conversation": "TRUE"}
            if (
                signal == "make_payment"
                and sub_intent == "affirm"
                and sub_context == "action_by_customer"
                and context == "payment"
            ):
                if entities:
                    for entity in entities:
                        if entity.get("entity", None) == "date":
                            date = True
                            given_date = datetime.datetime.strptime(
                                entity["value"], "%d/%m/%Y"
                            )
                            send_and_store_disposition_details(
                                tracker=tracker,
                                dispatcher=dispatcher,
                                flag=DEFAULT_FLAG,
                            )
                            return {"ask_followup_question": None,"go_to_form_slot":"deny", "stop_conversation": "TRUE"}
                        else:
                            send_and_store_disposition_details(
                                tracker=tracker,
                                dispatcher=dispatcher,
                                flag=DEFAULT_FLAG,
                                disposition_id="ATP"
                            )
                            return {"ask_followup_question": None,"go_to_form_slot":"aptp", "stop_conversation": "TRUE"}
                else:
                    send_and_store_disposition_details(
                        tracker=tracker,
                        dispatcher=dispatcher,
                        flag=DEFAULT_FLAG,
                        disposition_id="ATP"
                    )
                    return {"ask_followup_question": None,"go_to_form_slot":"aptp", "stop_conversation": "TRUE"}
        return {"ask_followup_question":None}
            
    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        back_to_partial_payment = tracker.get_slot("back_to_partial_payment")
        go_to_form = tracker.get_slot("go_to_form_slot")
        account_name = tracker.get_slot("account_name_slot")
        emi_flow = tracker.get_slot("emi_flow")
        script_type = tracker.get_slot("script_type_slot")
        variation = tracker.get_slot("variation_slot")
        if go_to_form == "aptp":
            if account_name == "Piramal Finance" or account_name == "Piramal Finance Testing":
                return [FollowupAction("ask_payment_method_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
            elif (emi_flow == "predue" and (account_name == "Bajaj Finserv" or account_name == "Bajaj Finserv Regional" or account_name == "Bajaj Finserv Testing")):
                return [FollowupAction("default_aptp_x_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
            elif ((account_name == "Aadhar Housing Finance" or account_name == "Aadhar Housing Finance Testing") and ("dpd" in emi_flow)) or account_name == "Bajaj Finserv" or account_name == "Bajaj Finserv Regional" or account_name == "Bajaj Finserv Testing" or account_name == "Sonata Finance" or account_name == "Sonata Finance Testing":
                return [FollowupAction("ask_payment_method_2_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
            else:
                return [FollowupAction("default_aptp_x_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
        if go_to_form == "deny":
            return [FollowupAction("councelling_v1_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
        if go_to_form == "payment_re_confirmation":
            return [FollowupAction("payment_re_confirmation_form"),SlotSet(REQUESTED_SLOT,None),SlotSet("trail_count",None),SlotSet("stop_conversation",None),SlotSet("go_to_form_slot",None),]
        return [FollowupAction("action_listen"), AllSlotsReset()]

from app.chatbot.chatbot_config import respond, usr
from app.NER.date_regex import find_date, later_date
from app.preprocessing.preprocessing import cool_preproc
from app.NER.cool_NER import extract, get_entity


def flight(usr_txt, _from=None, _to=None, _date=None, tries=0):

    def recheck(usr_txt, _from, _to, _date):
        parsed = cool_preproc(usr_txt)
        entities = extract(parsed)

        if not _from:
            _from = entities[0]
        if not _to:
            _to = entities[1]
        if not _date:
            _date = entities[2]

        return _from, _to, _date

    if not _from and not _to and not _date:

        if tries > 3:
            return "Sorry, I couldn't understand."
        else:
            parsed = cool_preproc(usr_txt)
            _from, _to, _date = extract(parsed)

    if not _from:
        respond("Where are you flying from?")
        usr_txt = input(usr)
        _from, _to, _date = recheck(usr_txt, _from, _to, _date)
        if not _from:
            _from = get_entity(usr_txt)
        return flight(usr_txt, _from, _to, _date, tries + 1)

    elif not _to:
        respond("Where are you flying to?")
        usr_txt = input(usr)
        _from, _to, _date = recheck(usr_txt, _from, _to, _date)
        if not _to:
            _to = get_entity(usr_txt)
        return flight(usr_txt, _from, _to, _date, tries + 1)

    elif _from.text.lower() == _to.text.lower():
        respond("The departure and destination cities can't be the same. Where are you flying to again?")
        usr_txt = input(usr)
        _to = get_entity(usr_txt)
        return flight(usr_txt, _from, _to, _date, tries + 1)

    elif not _date:
        respond("When do you want to go?")
        usr_txt = input(usr)
        _from, _to, _date = recheck(usr_txt, _from, _to, _date)
        if not _date:
            _date = find_date(usr_txt)
        return flight(usr_txt, _from, _to, _date, tries+1)

    elif not later_date(_date):
        respond("Sorry, the date has to be in the future.")
        usr_txt = input(usr)
        _from, _to, _date = recheck(usr_txt, _from, _to, _date)
        if not _date:
            _date = find_date(usr_txt)
        return flight(usr_txt, _from, _to, _date, tries+1)

    return "OK, looking for a %s-%s flight on %s." % (_from, _to, _date)


if __name__ == '__main__':
    string = "I want a flight from Lviv to Moscow on 8th of June, 2019"
    parsed = cool_preproc(string)

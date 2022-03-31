# Hour class, is loaded with all the needed data, used as a go-between the db and the pdf
class Breviary:
    OFFICE_OF_READINGS = "Office of Readings"
    MORNING_PRAYER = "Morning Prayer"
    DAYTIME_PRAYER = "Daytime Prayer"
    EVENING_PRAYER = "Evening Prayer"
    NIGHT_PRAYER = "Night Prayer"
    HOURS = [OFFICE_OF_READINGS, MORNING_PRAYER, DAYTIME_PRAYER, EVENING_PRAYER, NIGHT_PRAYER]

    SUNDAY = "Sunday"
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    DAYS = [SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY]

    Antiphon = {"title": "", "ant": ""}
    Psalm = {"titles": [], "verse": "", "summary": "", "summary_verse": "", "text": ""}
    Reading = {"verse": "", "text": ""}
    Response = {"verse": "", "response": ""}
    Intentions = {"first": "", "response": "", "intercessions": []}  # intercessions is list of Responses
    Hymn = {"name": "", "number": "", "saint_michaels_num": "", "in_ibrev": ""}


class Hour:
    def __init__(self):
        # this is the canonical variable_names should be used everythere!
        self.week = 0
        self.week_roman = ""
        self.day = ""
        self.hour = ""
        self.hymn = []  # List of Hymn type
        self.ant_1 = []  # List of Antiphon type
        self.ant_2 = []
        self.ant_3 = []
        self.ps_1 = Breviary.Psalm
        self.ps_2 = Breviary.Psalm
        self.ps_3 = Breviary.Psalm
        self.reading = Breviary.Reading
        self.response = []  # List of Response type
        self.canticle_ant = []  # List of Antiphon type
        self.intentions = Breviary.Intentions
        self.prayer = []  # List of Strings

    def process_row(self, row):
        pass


def fetch_rows(table="four_week"):
    import psycopg2
    import psycopg2.extras
    row = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres")
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cur.execute("SELECT * FROM " + table)
        row = cur.fetchone()
        # print(row["day"])
        # while row is not None:
        #    print(row)
        #    row = cur.fetchone()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()

    return row


def process_row(row):
    h = Hour()
    h.week = row["week"]
    if row["week"] == 1:
        h.week_roman = "I"
    elif row["week"] == 2:
        h.week_roman = "II"
    elif row["week"] == 5:
        h.week_roman = "III"
    elif row["week"] == 4:
        h.week_roman = "IV"

    h.day = row["day"]
    h.hour = row["hour"]

    h.hymn = row["hymn"]
    h.ant_1 = row["ant_1"]
    h.ant_2 = row["ant_2"]
    h.ant_3 = row["ant_3"]
    h.ps_1 = row["ps_1"]
    h.ps_2 = row["ps_2"]
    h.ps_3 = row["ps_3"]

    h.reading = row["reading"]

    h.response = row["response"]
    h.canticle_ant = row["canticle_ant"]

    h.intentions = row["intentions"]
    h.prayer = row["prayer"]

    return h

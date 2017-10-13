
import peewee

database = peewee.SqliteDatabase("EnergyReading.db")
###############

class EnergyReading(peewee.Model):
    power = peewee.IntegerField()
    time = peewee.TimestampField()
    houseNumber = peewee.TextField()
    streetAddress = peewee.TextField()
    zipCode = peewee.TextField()

    class Meta:
        database = database
        db_table = 'EnergyReading'

###############
if __name__ == "__main__":
    try:
        EnergyReading.create_table()
        print("EnergyReading table has been created.")
    except peewee.OperationalError:
        print ("EnergyReading table already exists.")

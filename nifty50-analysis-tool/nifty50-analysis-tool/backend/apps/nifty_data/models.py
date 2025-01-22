from djongo import models  

class NiftyData(models.Model):  
    timestamp = models.DateTimeField(auto_now_add=True)  
    open = models.FloatField()  
    close = models.FloatField()  
    high = models.FloatField()  
    low = models.FloatField()  
    volume = models.BigIntegerField()  

    class Meta:  
        db_table = 'nifty_data'  
        managed = False  # MongoDB handles schema  
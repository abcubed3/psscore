from django.db import models
#from publicservants import models
from django.utils.encoding import smart_unicode

# Create your models here.


class Score(models.Model):
    #score ID - publicservant ID plus score
    #sID = models.ManyToOneRel(field=PublicServant.psID)
    
    #PS Score at time t
    pst = models.IntegerField(null=False)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    #Factors that determine Public Servant Score, include Thumbs up or down on certain criterias.
    #Aggregrate values for period of time
    positivePersonality = models.IntegerField(null=False, blank=False)
    negativePersonality = models.IntegerField(null=False, blank=False)
    
    positiveReviewMentions = models.IntegerField(null=False, blank=False)
    negativeReviewMentions = models.IntegerField(null=False, blank=False)
    
    userScore= models.IntegerField(null=False, blank=False)
        
    #Actual PSScore at 12am everyday
    ps = models.IntegerField(null=False)
    
    def __unicode__(self):
        return smart_unicode(self.ps) # + smart_unicode(self.PublicServant.psID)
    
    
    
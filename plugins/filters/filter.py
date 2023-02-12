from datetime import datetime, timedelta

class FilterModule:
    '''
    CLASS DOCSTRING
    '''
    def filters(self):                                                       # pylint: disable=no-self-use
        '''
        METHOD DOCSTRING
        '''
        return {
            'getScheduleTime': FilterModule.getScheduleTime,
        }


    @staticmethod
    def getScheduleTime(hoursToAdd):
        '''Add Hours to utcnow() and return in YYYYMMDDTHHMMSSZ format for Tower
        job scheduling.        
        '''
        addedhours = datetime.utcnow() + timedelta(hours=int(hoursToAdd))
        return addedhours.strftime('%Y%m%dT%H%M%SZ')


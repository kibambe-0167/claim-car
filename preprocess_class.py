from sklearn.preprocessing import LabelEncoder, LabelEncoder, StandardScaler

_standardScalerObj = StandardScaler()

class Preprocss():
    '''preprocess features and scale them.'''
    def __init__(self):
        super().__init__()
        
    def __str__(self) -> str:
        return '''preprocess features and scale them.'''
        
    def transmission_type_norm(self, value ):
        '''0 -> automatic | 1 -> manuel'''
        value = str(value).lower()
        if 'automatic' == value: return 0
        elif 'manual' == value: return 1
        else: return 3
        
    def fuel_type_norm(self, value ):
        '''0 -> petrol | 1 ->diesel | 2 -> cng | 3 -> unknown '''
        value = str(value).lower()
        if value == 'petrol': return 0
        elif value == 'diesel': return 1
        elif value == 'cng': return 2
        else: return 3
    
    def speed_alert(self, value):
        '''0 -> No | 1 -> Yes'''
        value = str(value).lower()
        if value == 'no': return 0
        elif value == 'yes': return 1
        else: return 0
    
    def engine( self, value ):
        '''I can't use labelencoder from scikit-learn. its not optimal'''
        '''['F8D Petrol Engine', '1.2 L K12N Dualjet', '1.0 SCe',
       '1.5 L U2 CRDi', '1.5 Turbocharged Revotorq', 'K Series Dual jet',
       '1.2 L K Series Engine', 'K10C', 'i-DTEC', 'G12B',
       '1.5 Turbocharged Revotron']'''
        if value != None:
            value = str(value).lower()
            if value == 'f8d petrol engine'.lower(): return 0
            elif value == '1.2 L K12N Dualjet'.lower(): return 1
            elif value == '1.0 SCe'.lower(): return 2
            elif value == '1.5 L U2 CRDi'.lower(): return 3
            elif value == '1.5 Turbocharged Revotorq'.lower(): return 4
            elif value == 'K Series Dual jet'.lower(): return 5
            elif value == '1.2 L K Series Engine'.lower(): return 6
            elif value == 'K10C'.lower(): return 7
            elif value == 'i-DTEC'.lower(): return 8
            elif value == 'G12B'.lower(): return 9
            elif value == '1.5 Turbocharged Revotron'.lower(): return 10
        else: return value
        
    def standard_scaler(self, value ):
        '''use standard scaler to scal the age of the car'''
        array = [[value],]
        _standardScalerObj.fit(array)
        res = _standardScalerObj.transform(array)
        return res[0][0]
    
        
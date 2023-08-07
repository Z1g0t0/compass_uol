class Calculo:
    
    def soma(self, x, y):
        return x + y
        
    def sub(self, x, y):
        return abs(x-y)
     
C = Calculo()

x = 4 
y = 5

print('Somando:', x, '+', y, '=', C.soma(x,y))
print('Subtraindo:', x, '-', y, '=', C.sub(x,y))
#Hello! this code will give you the total molar mass of any compound. just respond to the prompts!

masses = [1.008,4.003,6.94,9.012,10.81,12.011,14.007,15.999,18.998,20.180,22.990,24.305,26.982,28.085,30.974,32.06,35.453,39.948,39.098,40.078,44.956,47.867,50.942,51.996,54.938,55.845,58.933,58.693,63.546,65.380,69.723,72.630,74.922,78,96,79.904,83.798]
masses.extend([85.467,87.621,88.909,91.224,92.906,95.951,98.0,101.072,102.905,106.421,107.868,112.414,114.818,118.711,121.760,127.603,126.904,131.294,132.905,137.328,138.905,140.116,140.908,144.242,145.0,150.362,151.964,157.253,158.925,162.500,164.930,167.259,168.934,173.045,174.967,178.492,180.978,183.841,186.207,190.233,192.217,195.085,196.967,200.592,204.38,207.21,208.980,209,210,222,223,226,227,232.038,231.036,238.029,237,244,243,247,247,251,252,257,258,259,266,267,268,269,270,277,278,281,282,285,286,289,290,293,294,294])

syms = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og']

def goodone():
    print('Please input a chemical formula of form "cu33h1" (no quotes needed).\nCase-insensitive. Cannot interpret parentheses (or charges or isotopes).\nFor elements with implied subscript `1`, please write the `1`.')
    formula = input("Chemical formula: ")
    args = []
    arg = ''
    hmm = 0
    while len(formula)>0:
        try:
            x = int(formula[0])
            formula = formula[1:]
            if arg == '':
                if type(args[-1]) == int:
                    args[-1] = args[-1]*10+x
                else:
                    args.append(x)
            else:
                args.append(arg)
                args.append(x)
                arg = ''
        except:
            arg = arg + formula[0]
            formula = formula[1:]
        hmm += 1
        assert hmm < 1000, 'You appear to be stuck in an infinite loop! Sorry! Or your formula is too long? Maybe double check the preconditions?'
    kwargs_mass(args)

def kwargs_mass(args):
    #print('args inputted were ',args)
    elem = ""
    quan = 0
    mass = 0
    #print('mass = zero')
    for arg in args:
        try:
            quan = int(arg)
            #print('try ',arg)
            elem = int(syms.index(elem.title()))
            #print('elem number',elem)
            elem_mass = masses[elem]
            #print('elem mass',elem_mass)
            mass += quan*elem_mass
            #print('mass +=',quan*elem_mass)
            quan = 0
            elem = ""
        except:
            #print('except ',arg)
            if elem != "":
                #print('elem != ""; elem =',elem) 
                quan = 1
                elem = int(syms.index(elem.title()))
                #print('on elem', elem)
                elem_mass = masses[elem]
                mass += quan*elem_mass
                #print('mass +=',quan*elem_mass)
                quan = 0
            elem = str(arg).lower()
    #print('finished For') 
    if (elem != ""):
        elem = int(syms.index(elem.title()))
        mass += masses[elem]
        #print('mass +=',masses[elem])
    print_mass(mass)

def print_mass(mass):
    print(mass, ' g/mol')
    print('This calculator is precise to the thousandth place.')

if __name__=='__main__':
    goodone()

''' A bunch of older stuff

def nextone(mass):
    an = input('atomic number or symbol: ')
    if ',' in an:
        args = [arg.strip() for arg in an.split(',')]
        # .replace("'","").replace('"','')
        kwargs_mass(args)
        return None
    if str(an) == '':
        #print_mass(mass)
        mass = 0
        return None
    elem = str(an).lower()
    elem = int(syms.index(elem.title()))
    quan = float(input('how many of these?'))
    elem_mass = masses[elem]
    mass += elem_mass * quan
    nextone(mass)

def forin():
    an = input('atomic number or symbol: ')
    #print('an is initially ' + str(an))
    args = [arg.strip() for arg in an.split(',')]
    #print('args inputted will be ',args)
    # .replace("'","").replace('"','')
    kwargs_mass(args)

def run(*args):
    """
    Finds the molar/molecular mass of any compound. Has three modes:
    
    With no initial arguments:
    When cycle is running, enter any valid atomic number or symbol (capitalization and quote marks will be discarded). submit a blank response for "a n o s" when done. Result will be printed.
    
    With one initial argument (INCOMPLETE! DO NOT USE!):
    Enter full molecular formula, non-subscripted numbers, case-insensitive. You must type a 1 after monatomic components, even where standard chemical notation would have it implied (I'm working on this). Result will be printed.
    To find the molar mass of Calcium Chloride, for instance, one would write run(Ca1Cl2)
    
    With multiple initial arguments:
    (Elements must be entered as strings. Sorry.)
    Enter full molecular formula, with commas between each element symbol and the quantity of that element. As in standard chemical notation, if there is no number following the element symbol, quantity==1 is implied.
    To find the molar mass of Calcium Chloride, for instance, one would write run(Ca,Cl,2)
    
    Note that element names can be repeated.
    """
    if args == ():
        nextone(0)
    #elif len(args) == 1:
    #    print("Sorry, do not yet have than functionality!")
    else:
        kwargs_mass([str(arg) for arg in args])

'''


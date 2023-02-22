def word(name,code):
    cs=[x for x in code.split(' ') if x!=""]
    o=""
    draw=0
    push=0
    change=0
    loopist=[]
    for i,block in enumerate(cs):
        cmd=cmds.get(block,'fail')
        if cmd=='fail':
            if block=='do':
                indent=1
                buf=[]
                i2=i
                while indent>0:
                    i2+=1
                    b2=cs[i2]
                    if b2=="do":
                        indent+=1
                    elif b2=="loop":
                        indent-=1
                    if indent>0:
                        buf.append(b2)
                d2,p2,c2=info(buf)
                if c2!=0:
                    raise SyntaxError('Looped functions must not change stack depth')
                if change+p2>push:
                    push=change+p2
                o+='<[-'+'>'*p2+'+'+'<'*p2+']'+'>'*p2+'[-'+'<'*p2
                loopist.append(p2)
                change-=1
            elif block=='loop':
                p2=loopist.pop(-1)
                o+='>'*p2+']'+'<'*p2
            else:
                try:
                    o+='+'*max(0,int(block))+'-'*max(0,-int(block))+'>'
                    change+=1
                    if change>push:
                        push=change
                except:
                    raise SyntaxError(f"Unknown function: '{block}'")
        else:
            o+=cmd[0]
            if change+cmd[1][1]>push:
                    push=change+cmd[1][1]
            if -change+cmd[1][0]>draw:
                    draw=-change+cmd[1][0]
            change+=cmd[1][2]
    cmds[name]=(o,(draw,push,change))
def info(tokens):
    draw=0
    push=0
    change=0
    loopist=[]
    for i,block in enumerate(tokens):
        cmd=cmds.get(block,'fail')
        if cmd=='fail':
            if block=='do':
                indent=1
                buf=[]
                i2=i
                while indent>0:
                    i2+=1
                    b2=cs[i2]
                    if b2=="do":
                        indent+=1
                    elif b2=="loop":
                        indent-=1
                    if indent>0:
                        buf.append(b2)
                d2,p2,c2=info(buf)
                if c2!=0:
                    raise SyntaxError('Looped functions must not change stack depth')
                if change+p2>push:
                    push=change+p2
                change-=1
            elif block=='loop':
                pass
            else:
                try:
                    change+=1
                    if change>push:
                        push=change
                except:
                    raise SyntaxError(f"Unknown function: '{block}'")
        else:
            if change+cmd[1][1]>push:
                    push=change+cmd[1][1]
            if -change+cmd[1][0]>draw:
                    draw=-change+cmd[1][0]
            change+=cmd[1][2]
    return((draw,push,change))

with open('specs.txt','r')as f:
    txt=f.read()
cmds={}
for line in txt.split('\n'):
    if line!="" and len(line)>2:
        if line[:2]!="//":
            a,b,c=line.split(':')
            c=[int(x) for x in c.split(',')]
            cmds[a]=(b,c)

code='2 3 *'

word('fib','swap 2_copy +')
word('*','0 swap do 2_copy + loop swap drop')
word('main',code)
        
        
print(cmds['main'])

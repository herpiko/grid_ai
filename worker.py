import sys
import time
from mpi4py import MPI

MPI.finalize = False
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if size < 2:
        print ''
        print ''
        print 'WARNING:'
        print ''
        print 'Should be run with minimal 2 node.'
        print ''
        print ''
        comm.Abort(0)

land = []
i = 1
while i < 401:
        land.append({'id':i, 'state' : ''})
        i += 1
robot = int(sys.argv[1])
target = int(sys.argv[2])
tembok = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,41,61,81,101,121,141,161,181,201,221,241,261,281,301,321,341,361,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380,400,43,44,63,83,45,85,105,125,125,124,123,107,87,67,143,163,183,142,222,223,224,185,165,166,167,147,169,207,206,246,24,27,49,69,70,109,108,58,57,36,56,98,76,96,75,74,72,54,136,137,114,134,135,92,112,91,31,32,71,131,149,170,154,174,190,127,68,210,307,308,309,310,290,270,250,291,292,293,332,352,350,349,369,347,325,345,365,305,285,284,323,343,322,263,245,247,268,248,283,172,192,212,213,214,252,232,255,275,254,333,334,374,368,176,196,197,159,237,238,297,317,317,318,316,338,358,279,278,356,357,199,179,178,99,139,217,277,313,231,230]
sudah = []
looping = False
pohon = []

#step

antrian = []
pernah = []
antrian_id = 1
loc = robot
y = False
x = False
q = 0
langkah = 1
ceksudah = False
ceksudahflag = False
sudahpernah = False
path = []


def istembok(id) :
    i = 0
    if id in tembok:
            return True
    else:
            return False

def determine_path():
    global path
    global pohon
    global rank
    print '--------------------------------------------------------------------------------'
    print 'DETERMINED PATH'
    xx = target
    aa = len(pohon) - 1
    bb = aa
    while bb > 0:
            if pohon[bb]['anak'] == xx :
                    xx = pohon[bb]['ortu']
                    path.append(xx)
            bb -= 1
    yy = 0
    while yy < len(path) :
            land[path[yy] - 1]['state'] = 'white'
            yy += 1

    print path
    print '--------------------------------------------------------------------------------'
    if size == 2:
            comm.send({'message' : 'stop'}, dest=0, tag=77)
            comm.Abort(0)
            sys.exit();

def bfs_step(rank):
        global loc
        global robot
        global target
        global tembok
        global sudah
        global looping
        global pohon
        global antrian
        global pernah
        global antrian_id
        global y
        global x
        global q
        global langkah
        global ceksudah
        global ceksudahflag
        global sudahpernah
        global path

        if loc != target :
                antrian_id = antrian_id + 1
                print('step for block : ' + str(loc))
                dest = 2
                if rank != 1:
                        dest = 1
                comm.send({'worker' : rank, 'last' : loc, 'pohon' : pohon, 'path' : path, 'message' : ''}, dest=0, tag=77)
                if istembok(loc) == False:
                        tembok.append(loc)

                        def check_around():
                            global antrian_id
                            if istembok(y) == False:
                                    sudahpernah = False
                                    tem = 0
                                    while tem < len(pernah) :
                                            if pernah[tem] == y :
                                                    sudahpernah = True
                                            tem += 1
                                    if sudahpernah == False :
                                            land[y-1]['state'] = 'green'
                                            antrian.append({'id':antrian_id, 'loc' : y })
                                            antrian_id = antrian_id + 1
                                            pernah.append(y)
                                            pohon.append({'ortu':loc, 'anak' : y})
                                            if y == target :
                                                    determine_path()


                        # ATAS
                        loc = loc
                        y = loc -20
                        check_around()

                        # KIRI
                        loc = loc
                        y = loc - 1
                        check_around()

                        # BAWAH
                        loc = loc
                        y = loc + 20
                        check_around()

                        # KANAN
                        loc = loc
                        y = loc + 1
                        check_around()

                        # Done chceking around

                        if ceksudahflag == True:
                                q += 1
                                ceksudahflag = False

                        q = q
                        if antrian:
                                loc = antrian[q]['loc']
                        tem = 0
                        while tem < len(tembok) :
                                if tembok[tem] == loc:
                                        ceksudah = True
                                tem += 1

                        if ceksudah == True:
                                if antrian:
                                        loc = antrian[q]['loc']
                                ceksudahflag = True
                                land[loc-1]['step'] = langkah
                                land[loc-1]['state'] = 'yellow'
                                if antrian:
                                        loc_ = antrian[1]['loc']
                                langkah += 1
                        else :
                                land[loc-1]['step'] = langkah;
                                land[loc-1]['state'] = 'yellow'
                                if antrian:
                                        loc_ = antrian[q]['loc']
                                langkah += 1
                q += 1



#fungsi gerak
def derajat0():
        id_now = id_current-1
        land[id_now].state = 'yellow'
        id_current = id_now
def derajat90():
        id_now = id_current-20
        land[id_now].state = 'yellow'
        id_current = id_now
def derajat180():
        id_now = id_current+1
        land[id_now].state = 'yellow'
        id_current = id_now
def derajat270():
        id_now = id_current+20
        land[id_now].state = 'yellow'
        id_current = id_now

def bfs_loop(rank) :
        while True:
                print 'worker : ' + str(rank)
                bfs_step(rank)
                time.sleep(0.02)



if rank == 0:
        worker1 = []
        worker2 = []
        while True:
                data = comm.recv(source=MPI.ANY_SOURCE, tag=77)
                if data['message'] == 'stop':
                        comm.Abort(0)
                        sys.exit()
                print('data from worker : ' + str(data))
                if data['worker'] == 1:
                        worker1.append(int(data['last']))
                        worker1_last_data = data
                        if int(data['last']) in worker2:
                                target = data['last']
                                pohon = worker1_last_data['pohon']
                                determine_path()
                                pohon = worker2_last_data['pohon']
                                path = []
                                determine_path()
                                comm.Abort(0);
                                sys.exit();
                if data['worker'] == 2:
                        worker2.append(int(data['last']))
                        worker2_last_data = data
                        if int(data['last']) in worker1:
                                target = data['last']
                                pohon = worker1_last_data['pohon']
                                determine_path()
                                path = []
                                pohon = worker2_last_data['pohon']
                                determine_path()
                                comm.Abort(0);
                                sys.exit();
                time.sleep(0.01);
else:
        if rank % 2 == 0:
                target_ = target
                target = robot
                robot = target_
                loc = robot
        bfs_loop(rank)


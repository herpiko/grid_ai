__all__ = ['worker']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
import sys
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

def bfs(rank_node):
    print rank_node
    # setting scope
    var = Scope( JS_BUILTINS )
    set_global_object(var)

    # Code follows:
    var.registers([u'tembok', u'looping', u'sudahpernah', u'ceksudah', u'ceksudahflag', u'derajat180', u'loc', u'sudah', u'langkah', u'derajat270', u'derajat0', u'antrian', u'istembok', u'bfs_loop', u'determine_path', u'derajat90', u'bfs_step', u'path', u'pohon', u'antrian_id', u'pernah', u'land', u'target', u'i', u'robot', u'q', u'y', u'x'])
    @Js
    def PyJsHoisted_derajat0_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.put(u'id_now', (var.get(u'id_current')-Js(1.0)))
        var.get(u'land').get(var.get(u'parseInt')(var.get(u'id_now'))).put(u'state', Js(u'yellow'))
        var.put(u'id_current', var.get(u'id_now'))
    PyJsHoisted_derajat0_.func_name = u'derajat0'
    var.put(u'derajat0', PyJsHoisted_derajat0_)
    @Js
    def PyJsHoisted_istembok_(id, this, arguments, var=var):
        var = Scope({u'this':this, u'id':id, u'arguments':arguments}, var)
        var.registers([u'i', u'id'])
        pass
        #for JS loop
        var.put(u'i', Js(0.0))
        while (var.get(u'i')<Js(400.0)):
            try:
                if (var.get(u'id')==var.get(u'tembok').get(var.get(u'i'))):
                    return var.get(u'true')
            finally:
                    (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
    PyJsHoisted_istembok_.func_name = u'istembok'
    var.put(u'istembok', PyJsHoisted_istembok_)
    @Js
    def PyJsHoisted_bfs_loop_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        while var.get(u'true'):
            var.get(u'bfs_step')()
    PyJsHoisted_bfs_loop_.func_name = u'bfs_loop'
    var.put(u'bfs_loop', PyJsHoisted_bfs_loop_)
    @Js
    def PyJsHoisted_determine_path_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'yy', u'aa', u'xx', u'bb', u'zz'])
        pass
        pass
        pass
        var.put(u'xx', var.get(u'target'))
        pass
        var.put(u'aa', (var.get(u'pohon').get(u'length')-Js(1.0)))
        #for JS loop
        var.put(u'bb', var.get(u'aa'))
        while (var.get(u'bb')>Js(0.0)):
            try:
                if (var.get(u'pohon').get(var.get(u'bb')).get(u'anak')==var.get(u'xx')):
                    var.put(u'xx', var.get(u'pohon').get(var.get(u'bb')).get(u'ortu'))
                    var.get(u'path').callprop(u'push', var.get(u'xx'))
            finally:
                    (var.put(u'bb',Js(var.get(u'bb').to_number())-Js(1))+Js(1))
        #for JS loop
        var.put(u'yy', Js(0.0))
        while (var.get(u'yy')<var.get(u'path').get(u'length')):
            try:
                var.get(u'land').get((var.get(u'parseInt')(var.get(u'path').get(var.get(u'yy')))-Js(1.0))).put(u'state', Js(u'white'))
            finally:
                    (var.put(u'yy',Js(var.get(u'yy').to_number())+Js(1))-Js(1))
        var.get(u'console').callprop(u'log', (Js(u'result : ')+var.get(u'path')))
    PyJsHoisted_determine_path_.func_name = u'determine_path'
    var.put(u'determine_path', PyJsHoisted_determine_path_)
    @Js
    def PyJsHoisted_bfs_step_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([u'tem', u'loc_'])
        class JS_BREAK_LABEL_627265616b706f696e74(Exception): pass
        try:
            if (var.get(u'parseInt')(var.get(u'loc'))==var.get(u'parseInt')(var.get(u'target'))):
                pass
            else:
                var.put(u'antrian_id', (var.get(u'parseInt')(var.get(u'antrian_id'))+Js(1.0)))
                #var.get(u'console').callprop(u'log', (Js(u'step for block : ')+var.get(u'loc')))
                print('step for block : ' + str(var.get(u'loc')))
                if var.get(u'istembok')(var.get(u'loc')).neg():
                    var.get(u'tembok').callprop(u'push', var.get(u'parseInt')(var.get(u'loc')))
                    var.put(u'loc', var.get(u'parseInt')(var.get(u'loc')))
                    var.put(u'y', (var.get(u'loc')-Js(20.0)))
                    if var.get(u'istembok')(var.get(u'y')).neg():
                        pass
                        var.put(u'sudahpernah', Js(False))
                        #for JS loop
                        var.put(u'tem', Js(0.0))
                        while (var.get(u'tem')<var.get(u'pernah').get(u'length')):
                            try:
                                if (var.get(u'parseInt')(var.get(u'pernah').get(var.get(u'tem')))==var.get(u'parseInt')(var.get(u'y'))):
                                    var.put(u'sudahpernah', var.get(u'true'))
                            finally:
                                    (var.put(u'tem',Js(var.get(u'tem').to_number())+Js(1))-Js(1))
                        if var.get(u'sudahpernah').neg():
                            var.get(u'land').get((var.get(u'parseInt')(var.get(u'y'))-Js(1.0))).put(u'state', Js(u'green'))
                            PyJs_Object_1_ = Js({u'id':var.get(u'antrian_id'),u'loc':var.get(u'y')})
                            var.get(u'antrian').callprop(u'push', PyJs_Object_1_)
                            var.put(u'antrian_id', (var.get(u'parseInt')(var.get(u'antrian_id'))+Js(1.0)))
                            var.get(u'pernah').callprop(u'push', var.get(u'parseInt')(var.get(u'y')))
                            PyJs_Object_2_ = Js({u'ortu':var.get(u'loc'),u'anak':var.get(u'y')})
                            var.get(u'pohon').callprop(u'push', PyJs_Object_2_)
                            if (var.get(u'y')==var.get(u'target')):
                                var.get(u'determine_path')()
                                #var.get(u'process').callprop(u'exit')
                                sys.exit(0)
                                raise JS_BREAK_LABEL_627265616b706f696e74("Breaked")
                        else:
                            pass
                    var.put(u'loc', var.get(u'parseInt')(var.get(u'loc')))
                    var.put(u'y', (var.get(u'loc')-Js(1.0)))
                    if var.get(u'istembok')(var.get(u'y')).neg():
                        pass
                        var.put(u'sudahpernah', Js(False))
                        #for JS loop
                        var.put(u'tem', Js(0.0))
                        while (var.get(u'tem')<var.get(u'pernah').get(u'length')):
                            try:
                                if (var.get(u'parseInt')(var.get(u'pernah').get(var.get(u'tem')))==var.get(u'parseInt')(var.get(u'y'))):
                                    var.put(u'sudahpernah', var.get(u'true'))
                            finally:
                                    (var.put(u'tem',Js(var.get(u'tem').to_number())+Js(1))-Js(1))
                        if var.get(u'sudahpernah').neg():
                            var.get(u'land').get((var.get(u'parseInt')(var.get(u'y'))-Js(1.0))).put(u'state', Js(u'green'))
                            PyJs_Object_3_ = Js({u'id':var.get(u'antrian_id'),u'loc':var.get(u'y')})
                            var.get(u'antrian').callprop(u'push', PyJs_Object_3_)
                            var.put(u'antrian_id', (var.get(u'parseInt')(var.get(u'antrian_id'))+Js(1.0)))
                            var.get(u'pernah').callprop(u'push', var.get(u'parseInt')(var.get(u'y')))
                            PyJs_Object_4_ = Js({u'ortu':var.get(u'loc'),u'anak':var.get(u'y')})
                            var.get(u'pohon').callprop(u'push', PyJs_Object_4_)
                            if (var.get(u'y')==var.get(u'target')):
                                var.get(u'determine_path')()
                                #var.get(u'process').callprop(u'exit')
                                sys.exit(0)
                                raise JS_BREAK_LABEL_627265616b706f696e74("Breaked")
                        else:
                            pass
                    var.put(u'loc', var.get(u'parseInt')(var.get(u'loc')))
                    var.put(u'y', (var.get(u'loc')+Js(20.0)))
                    if var.get(u'istembok')(var.get(u'y')).neg():
                        pass
                        var.put(u'sudahpernah', Js(False))
                        #for JS loop
                        var.put(u'tem', Js(0.0))
                        while (var.get(u'tem')<var.get(u'pernah').get(u'length')):
                            try:
                                if (var.get(u'parseInt')(var.get(u'pernah').get(var.get(u'tem')))==var.get(u'parseInt')(var.get(u'y'))):
                                    var.put(u'sudahpernah', var.get(u'true'))
                            finally:
                                    (var.put(u'tem',Js(var.get(u'tem').to_number())+Js(1))-Js(1))
                        if var.get(u'sudahpernah').neg():
                            var.get(u'land').get((var.get(u'parseInt')(var.get(u'y'))-Js(1.0))).put(u'state', Js(u'green'))
                            PyJs_Object_5_ = Js({u'id':var.get(u'antrian_id'),u'loc':var.get(u'y')})
                            var.get(u'antrian').callprop(u'push', PyJs_Object_5_)
                            var.put(u'antrian_id', (var.get(u'parseInt')(var.get(u'antrian_id'))+Js(1.0)))
                            var.get(u'pernah').callprop(u'push', var.get(u'parseInt')(var.get(u'y')))
                            PyJs_Object_6_ = Js({u'ortu':var.get(u'loc'),u'anak':var.get(u'y')})
                            var.get(u'pohon').callprop(u'push', PyJs_Object_6_)
                            if (var.get(u'y')==var.get(u'target')):
                                var.get(u'determine_path')()
                                var.get(u'console').callprop(u'log', Js(u'Target udah ketemu!'))
                                var.get(u'console').callprop(u'log', var.get(u'path'))
                                #var.get(u'process').callprop(u'exit')
                                sys.exit(0)
                                raise JS_BREAK_LABEL_627265616b706f696e74("Breaked")
                        else:
                            pass
                    var.put(u'loc', var.get(u'parseInt')(var.get(u'loc')))
                    var.put(u'y', (var.get(u'loc')+Js(1.0)))
                    if var.get(u'istembok')(var.get(u'y')).neg():
                        pass
                        var.put(u'sudahpernah', Js(False))
                        #for JS loop
                        var.put(u'tem', Js(0.0))
                        while (var.get(u'tem')<var.get(u'pernah').get(u'length')):
                            try:
                                if (var.get(u'parseInt')(var.get(u'pernah').get(var.get(u'tem')))==var.get(u'parseInt')(var.get(u'y'))):
                                    var.put(u'sudahpernah', var.get(u'true'))
                            finally:
                                    (var.put(u'tem',Js(var.get(u'tem').to_number())+Js(1))-Js(1))
                        if var.get(u'sudahpernah').neg():
                            var.get(u'land').get((var.get(u'parseInt')(var.get(u'y'))-Js(1.0))).put(u'state', Js(u'green'))
                            PyJs_Object_7_ = Js({u'id':var.get(u'antrian_id'),u'loc':var.get(u'y')})
                            var.get(u'antrian').callprop(u'push', PyJs_Object_7_)
                            var.put(u'antrian_id', (var.get(u'parseInt')(var.get(u'antrian_id'))+Js(1.0)))
                            var.get(u'pernah').callprop(u'push', var.get(u'parseInt')(var.get(u'y')))
                            PyJs_Object_8_ = Js({u'ortu':var.get(u'loc'),u'anak':var.get(u'y')})
                            var.get(u'pohon').callprop(u'push', PyJs_Object_8_)
                            if (var.get(u'y')==var.get(u'target')):
                                var.get(u'determine_path')()
                                #var.get(u'process').callprop(u'exit')
                                sys.exit(0)
                                raise JS_BREAK_LABEL_627265616b706f696e74("Breaked")
                        else:
                            pass
                    if var.get(u'ceksudahflag'):
                        (var.put(u'q',Js(var.get(u'q').to_number())+Js(1))-Js(1))
                        var.put(u'ceksudahflag', Js(False))
                    var.put(u'q', var.get(u'parseInt')(var.get(u'q')))
                    var.put(u'loc', var.get(u'antrian').get(var.get(u'q')).get(u'loc'))
                    pass
                    #for JS loop
                    var.put(u'tem', Js(0.0))
                    while (var.get(u'tem')<var.get(u'tembok').get(u'length')):
                        try:
                            if (var.get(u'parseInt')(var.get(u'tembok').get(var.get(u'tem')))==var.get(u'parseInt')(var.get(u'loc'))):
                                var.put(u'ceksudah', var.get(u'true'))
                        finally:
                                (var.put(u'tem',Js(var.get(u'tem').to_number())+Js(1))-Js(1))
                    if var.get(u'ceksudah'):
                        var.put(u'loc', var.get(u'parseInt')(var.get(u'antrian').get(var.get(u'q')).get(u'loc')))
                        var.put(u'loc', Js(u''))
                        var.put(u'loc', var.get(u'parseInt')(var.get(u'antrian').get(var.get(u'q')).get(u'loc')))
                        var.put(u'ceksudahflag', var.get(u'true'))
                        var.get(u'land').get((var.get(u'parseInt')(var.get(u'loc'))-Js(1.0))).put(u'step', var.get(u'langkah'))
                        var.get(u'land').get((var.get(u'parseInt')(var.get(u'loc'))-Js(1.0))).put(u'state', Js(u'yellow'))
                        var.put(u'loc_', var.get(u'parseInt')(var.get(u'antrian').get(var.get(u'q')).get(u'loc')))
                        (var.put(u'langkah',Js(var.get(u'langkah').to_number())+Js(1))-Js(1))
                    else:
                        var.get(u'land').get((var.get(u'parseInt')(var.get(u'loc'))-Js(1.0))).put(u'step', var.get(u'langkah'))
                        var.get(u'land').get((var.get(u'parseInt')(var.get(u'loc'))-Js(1.0))).put(u'state', Js(u'yellow'))
                        var.put(u'loc_', var.get(u'parseInt')(var.get(u'antrian').get(var.get(u'q')).get(u'loc')))
                        (var.put(u'langkah',Js(var.get(u'langkah').to_number())+Js(1))-Js(1))
                else:
                    pass
                (var.put(u'q',Js(var.get(u'q').to_number())+Js(1))-Js(1))
        except JS_BREAK_LABEL_627265616b706f696e74:
            pass
    PyJsHoisted_bfs_step_.func_name = u'bfs_step'
    var.put(u'bfs_step', PyJsHoisted_bfs_step_)
    @Js
    def PyJsHoisted_derajat90_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.put(u'id_now', (var.get(u'id_current')-Js(20.0)))
        var.get(u'land').get(var.get(u'parseInt')(var.get(u'id_now'))).put(u'state', Js(u'yellow'))
        var.put(u'id_current', var.get(u'id_now'))
    PyJsHoisted_derajat90_.func_name = u'derajat90'
    var.put(u'derajat90', PyJsHoisted_derajat90_)
    @Js
    def PyJsHoisted_derajat180_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.put(u'id_now', (var.get(u'id_current')+Js(1.0)))
        var.get(u'land').get(var.get(u'parseInt')(var.get(u'id_now'))).put(u'state', Js(u'yellow'))
        var.put(u'id_current', var.get(u'id_now'))
    PyJsHoisted_derajat180_.func_name = u'derajat180'
    var.put(u'derajat180', PyJsHoisted_derajat180_)
    @Js
    def PyJsHoisted_derajat270_(this, arguments, var=var):
        var = Scope({u'this':this, u'arguments':arguments}, var)
        var.registers([])
        var.put(u'id_now', (var.get(u'id_current')+Js(20.0)))
        var.get(u'land').get(var.get(u'parseInt')(var.get(u'id_now'))).put(u'state', Js(u'yellow'))
        var.put(u'id_current', var.get(u'id_now'))
    PyJsHoisted_derajat270_.func_name = u'derajat270'
    var.put(u'derajat270', PyJsHoisted_derajat270_)
    var.put(u'land', Js([]))
    #for JS loop
    var.put(u'i', Js(1.0))
    while (var.get(u'i')<=Js(400.0)):
        try:
            PyJs_Object_0_ = Js({u'id':var.get(u'i')})
            var.get(u'land').callprop(u'push', PyJs_Object_0_)
        finally:
                (var.put(u'i',Js(var.get(u'i').to_number())+Js(1))-Js(1))
    var.put(u'robot', Js(23.0))
    var.put(u'target', Js(298.0))
    var.put(u'tembok', Js([Js(1.0), Js(2.0), Js(3.0), Js(4.0), Js(5.0), Js(6.0), Js(7.0), Js(8.0), Js(9.0), Js(10.0), Js(11.0), Js(12.0), Js(13.0), Js(14.0), Js(15.0), Js(16.0), Js(17.0), Js(18.0), Js(19.0), Js(20.0), Js(21.0), Js(41.0), Js(61.0), Js(81.0), Js(101.0), Js(121.0), Js(141.0), Js(161.0), Js(181.0), Js(201.0), Js(221.0), Js(241.0), Js(261.0), Js(281.0), Js(301.0), Js(321.0), Js(341.0), Js(361.0), Js(381.0), Js(382.0), Js(383.0), Js(384.0), Js(385.0), Js(386.0), Js(387.0), Js(388.0), Js(389.0), Js(390.0), Js(391.0), Js(392.0), Js(393.0), Js(394.0), Js(395.0), Js(396.0), Js(397.0), Js(398.0), Js(399.0), Js(40.0), Js(60.0), Js(80.0), Js(100.0), Js(120.0), Js(140.0), Js(160.0), Js(180.0), Js(200.0), Js(220.0), Js(240.0), Js(260.0), Js(280.0), Js(300.0), Js(320.0), Js(340.0), Js(360.0), Js(380.0), Js(400.0), Js(43.0), Js(44.0), Js(63.0), Js(83.0), Js(45.0), Js(85.0), Js(105.0), Js(125.0), Js(125.0), Js(124.0), Js(123.0), Js(107.0), Js(87.0), Js(67.0), Js(143.0), Js(163.0), Js(183.0), Js(142.0), Js(222.0), Js(223.0), Js(224.0), Js(185.0), Js(165.0), Js(166.0), Js(167.0), Js(147.0), Js(169.0), Js(207.0), Js(206.0), Js(246.0), Js(24.0), Js(27.0), Js(49.0), Js(69.0), Js(70.0), Js(109.0), Js(108.0), Js(58.0), Js(57.0), Js(36.0), Js(56.0), Js(98.0), Js(76.0), Js(96.0), Js(75.0), Js(74.0), Js(72.0), Js(54.0), Js(136.0), Js(137.0), Js(114.0), Js(134.0), Js(135.0), Js(92.0), Js(112.0), Js(91.0), Js(31.0), Js(32.0), Js(71.0), Js(131.0), Js(149.0), Js(170.0), Js(154.0), Js(174.0), Js(190.0), Js(127.0), Js(68.0), Js(210.0), Js(307.0), Js(308.0), Js(309.0), Js(310.0), Js(290.0), Js(270.0), Js(250.0), Js(291.0), Js(292.0), Js(293.0), Js(332.0), Js(352.0), Js(350.0), Js(349.0), Js(369.0), Js(347.0), Js(325.0), Js(345.0), Js(365.0), Js(305.0), Js(285.0), Js(284.0), Js(323.0), Js(343.0), Js(322.0), Js(263.0), Js(245.0), Js(247.0), Js(268.0), Js(248.0), Js(283.0), Js(172.0), Js(192.0), Js(212.0), Js(213.0), Js(214.0), Js(252.0), Js(232.0), Js(255.0), Js(275.0), Js(254.0), Js(333.0), Js(334.0), Js(374.0), Js(368.0), Js(176.0), Js(196.0), Js(197.0), Js(159.0), Js(237.0), Js(238.0), Js(297.0), Js(317.0), Js(317.0), Js(318.0), Js(316.0), Js(338.0), Js(358.0), Js(279.0), Js(278.0), Js(356.0), Js(357.0), Js(199.0), Js(179.0), Js(178.0), Js(99.0), Js(139.0), Js(217.0), Js(277.0), Js(313.0), Js(231.0), Js(230.0)]))
    var.put(u'sudah', Js([]))
    var.put(u'pohon', Js([]))
    var.put(u'antrian', Js([]))
    var.put(u'pernah', Js([]))
    var.put(u'antrian_id', Js(1.0))
    var.put(u'loc', var.get(u'robot'))
    var.put(u'q', Js(0.0))
    var.put(u'langkah', Js(1.0))
    var.put(u'ceksudahflag', Js(False))
    var.put(u'sudahpernah', Js(False))
    var.put(u'path', Js([]))

    var.get(u'bfs_loop')()


    # Add lib to the module scope
    worker = var.to_python()

bfs(rank)

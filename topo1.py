from mininet.topo import Topo


class MyTopo(Topo):
    def __init__(self):

        # Initialize topology
        Topo.__init__(self)

        
        mainswitch  = self.addSwitch('s1')

        for i in range(1,5):
            newSwitch =self.addSwitch("SW1c{}".format(i))     
            self.addLink(mainswitch,newSwitch)
            for j in range(1,5):
                newHost = self.addHost("PC{}c{}".format(i,j))
                self.addLink(newSwitch, newHost)

topos = {'mytopo': (lambda: MyTopo())}
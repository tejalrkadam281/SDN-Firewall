from mininet.topo import Topo

class MyTopo(Topo):
    def __init__(self):

        # Initialize topology
        Topo.__init__(self)

        
        # mainswitch  = self.addSwitch('s1')
        h1 = self.addHost( 'PC1c1', ip='10.0.0.1', mac='00:00:00:00:00:01' )
        h2 = self.addHost( 'PC1c2', ip='10.0.0.2', mac='00:00:00:00:00:02' )
        h3 = self.addHost( 'PC1c3', ip='10.0.0.3', mac='00:00:00:00:00:03' )
        h4 = self.addHost( 'PC1c4', ip='10.0.0.4', mac='00:00:00:00:00:04' )
        h5 = self.addHost( 'PC2c1', ip='10.0.0.5', mac='00:00:00:00:00:05' )
        h6 = self.addHost( 'PC2c2', ip='10.0.0.6', mac='00:00:00:00:00:06' )
        h7 = self.addHost( 'PC2c3', ip='10.0.0.7', mac='00:00:00:00:00:07' )
        h8 = self.addHost( 'PC2c4', ip='10.0.0.8', mac='00:00:00:00:00:08' )
        h9 = self.addHost( 'PC3c1', ip='10.0.0.9', mac='00:00:00:00:00:09' )
        h10 = self.addHost( 'PC3c2', ip='10.0.0.10', mac='00:00:00:00:00:10' )
        h11 = self.addHost( 'PC3c3', ip='10.0.0.11', mac='00:00:00:00:00:11' )
        h12 = self.addHost( 'PC3c4', ip='10.0.0.12', mac='00:00:00:00:00:12' )
        h13 = self.addHost( 'PC4c1', ip='10.0.0.13', mac='00:00:00:00:00:13' )
        h14 = self.addHost( 'PC4c2', ip='10.0.0.14', mac='00:00:00:00:00:14' )
        h15 = self.addHost( 'PC4c3', ip='10.0.0.15', mac='00:00:00:00:00:15' )
        h16 = self.addHost( 'PC4c4', ip='10.0.0.16', mac='00:00:00:00:00:16' )
        s1 = self.addSwitch( 's1')
        s2 = self.addSwitch( 'SW1c1')
        s3 = self.addSwitch( 'SW1c2')
        s4 = self.addSwitch( 'SW1c3')
        s5 = self.addSwitch( 'SW1c4')
        self.addLink(s1,s2)
        self.addLink(s1,s3)
        self.addLink(s1,s4)
        self.addLink(s1,s5)

        self.addLink(s2,h1)
        self.addLink(s2,h2)
        self.addLink(s2,h3)
        self.addLink(s2,h4)
        
        self.addLink(s3,h5)
        self.addLink(s3,h6)
        self.addLink(s3,h7)
        self.addLink(s3,h8)

        self.addLink(s4,h9)
        self.addLink(s4,h10)
        self.addLink(s4,h11)
        self.addLink(s4,h12)

        self.addLink(s5,h13)
        self.addLink(s5,h14)
        self.addLink(s5,h15)
        self.addLink(s5,h16)

        # iter=0
        # for i in range(1,5):
        #     newSwitch =self.addSwitch("SW1c{}".format(i))     
        #     self.addLink(mainswitch,newSwitch)
        #     for j in range(1,5):
        #         iter = iter + 1
        #         if(iter <= 9):
        #             macad = '00:00:00:00:00:0{}'.format(iter)
        #             newHost = self.addHost("PC{}c{}".format(i,j), ip='10.0.0.{}'.format(iter), mac=macad)
        #         else:
        #             newHost = self.addHost("PC{}c{}".format(i,j), ip='10.0.0.{}'.format(iter), mac='00:00:00:00:00:{}'.format(iter))
        #         self.addLink(newSwitch, newHost)

topos = {'mytopo': (lambda: MyTopo())}

# sudo mn --custom exampletop.py --topo mytopo
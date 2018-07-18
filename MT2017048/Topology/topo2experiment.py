#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=Controller,
                      protocol='tcp',
                      port=6653,
		      ip='192.168.122.1')

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h19 = net.addHost('h19', cls=Host, ip='10.0.0.19', defaultRoute=None)
    h29 = net.addHost('h29', cls=Host, ip='10.0.0.29', defaultRoute=None)
    h17 = net.addHost('h17', cls=Host, ip='10.0.0.17', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h25 = net.addHost('h25', cls=Host, ip='10.0.0.25', defaultRoute=None)
    h27 = net.addHost('h27', cls=Host, ip='10.0.0.27', defaultRoute=None)
    h24 = net.addHost('h24', cls=Host, ip='10.0.0.24', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h34 = net.addHost('h34', cls=Host, ip='10.0.0.34', defaultRoute=None)
    h22 = net.addHost('h22', cls=Host, ip='10.0.0.22', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h30 = net.addHost('h30', cls=Host, ip='10.0.0.30', defaultRoute=None)
    h32 = net.addHost('h32', cls=Host, ip='10.0.0.32', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h20 = net.addHost('h20', cls=Host, ip='10.0.0.20', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h33 = net.addHost('h33', cls=Host, ip='10.0.0.33', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.16', defaultRoute=None)
    h18 = net.addHost('h18', cls=Host, ip='10.0.0.18', defaultRoute=None)
    h31 = net.addHost('h31', cls=Host, ip='10.0.0.31', defaultRoute=None)
    h23 = net.addHost('h23', cls=Host, ip='10.0.0.23', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h26 = net.addHost('h26', cls=Host, ip='10.0.0.26', defaultRoute=None)
    h21 = net.addHost('h21', cls=Host, ip='10.0.0.21', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h28 = net.addHost('h28', cls=Host, ip='10.0.0.28', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(h24, s1)
    net.addLink(h28, s1)
    net.addLink(h29, s1)
    net.addLink(h25, s1)
    net.addLink(h26, s1)
    net.addLink(h27, s1)
    net.addLink(s1, s7)
    net.addLink(s8, s3)
    net.addLink(s8, s4)
    net.addLink(s6, s7)
    net.addLink(s5, h11)
    net.addLink(s5, h7)
    net.addLink(s5, h8)
    net.addLink(s5, h10)
    net.addLink(s5, h9)
    net.addLink(s4, h12)
    net.addLink(s4, h13)
    net.addLink(s4, h14)
    net.addLink(s4, h15)
    net.addLink(s4, h16)
    net.addLink(s3, h17)
    net.addLink(s3, h18)
    net.addLink(s3, h19)
    net.addLink(s3, h20)
    net.addLink(s3, h21)
    net.addLink(s3, h23)
    net.addLink(s3, h22)
    net.addLink(s2, h34)
    net.addLink(s2, h33)
    net.addLink(s2, h30)
    net.addLink(s2, h31)
    net.addLink(s2, h32)
    net.addLink(s6, h5)
    net.addLink(s6, h1)
    net.addLink(s6, h2)
    net.addLink(s6, h3)
    net.addLink(s6, h4)
    net.addLink(s6, h6)
    net.addLink(s7, s2)
    net.addLink(s8, s2)
    net.addLink(s5, s8)
    net.addLink(s7, s5)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s7').start([c0])
    net.get('s6').start([c0])
    net.get('s8').start([c0])
    net.get('s5').start([c0])
    net.get('s3').start([c0])
    net.get('s4').start([c0])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()


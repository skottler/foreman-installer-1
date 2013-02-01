class { foreman_proxy:
  servername => "192.168.100.1",
  port => 9090,
  puppetca => false,
  dhcp => true,
  dhcp_interface => "virbr1",
  dns => true,
  dns_interface => "virbr1",
  tftp => true }

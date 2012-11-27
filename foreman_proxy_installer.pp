class { foreman_proxy:
  dhcp => true,
  dhcp_interface => "eth1",
  dns => true,
  dns_interface => "eth1",
  tftp => true }

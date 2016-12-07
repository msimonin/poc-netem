#!/usr/bin/env ruby

require 'json'

# getting all ips
ips=%x[vagrant ssh-config | grep HostName | awk '{print $2}']
ips = ips.split("\n")

constraints = []
ips.each_with_index do |ip1, index1|
  puts ip1
  ips.each_with_index do |ip2, index2|
    if ip1 == ip2
      next
    end
    constraints << {
      :source => ip1,
      :target => ip2,
      :rate =>"#{index1 * index2 + 5}Mbit",
      :delay => "#{index1 * index2 * 10 + 30}ms"
    }
  end
end
constraints = {
  :tc => constraints
}

File.open('constraints.yml', 'w') {|f| f.write JSON.pretty_generate(constraints) } 

# generate the inventory
# we by pass vagrant support because it's too slow (sequential)
inventory = ["[test]"]
ips.each_with_index do |ip, index|
  inventory << "netem#{index} ansible_host=#{ip} ansible_user=vagrant"
end
inventory << "[test:vars]"
inventory << "ansible_ssh_common_args='-o IdentityFile=\"/Users/msimonin/.vagrant.d/insecure_private_key\" -o ProxyCommand=\"ssh -W %h:%p msimonin@access.grid5000.fr\"'"

File.open('inventory.generated', 'w') {|f| f.write inventory.join("\n")}



# -*- mode: ruby -*-
# vi: set ft=ruby :


NB=10
Vagrant.configure(2) do |config|

    ## This define a VM.
    ## a g5k provider section will override top level options
    ## To define multiple VMs you can
    ## * either repeat the block
    ## * loop over using (1..N).each block
    (0..NB-1).each do |i|
      config.vm.define "netem#{i}" do |my|
        my.vm.box = "dummy"

        my.vm.provider "g5k" do |g5k|
          # project id must be unique accross all
          # your projects using vagrant-g5k to avoid conflict
          # on vm disks
          g5k.project_id = "test-vagrant-g5k"
          #g5k.site = "igrida"
          g5k.site = "rennes"
          g5k.username = "msimonin"
          g5k.gateway = "access.grid5000.fr"
          g5k.walltime = "03:00:00"

          # Image backed on the frontend filesystem
          g5k.image = {
            :path    => "public/ubuntu1404-9p.qcow2",
            :backing => "snapshot"
          }

          ## Bridged network : this allow VMs to communicate
          g5k.net = {
            :type => "bridge"
          }

          ## Nat network : VMs will only have access to the external world
          ## Forwarding ports will allow you to access services hosted inside the
          ## VM.
          #g5k.net = {
          #  :type => "nat",
          #  :ports => ["222#{i}-:22"]
          #}

          ## OAR selection of resource
          g5k.oar = "virtual != 'None'"
          #g5k.oar = "network_address in ('igrida05-04.irisa.fr')"

          ## VM size customization default values are
          ## cpu => -1 -> all the cpu of the reserved node
          ## mem => -1 -> all the mem of the reserved node
          ##
          #g5k.resources = {
          #  :cpu => 1,
          #  :mem => 1024
          #}
        end #g5k

      end

    end
end

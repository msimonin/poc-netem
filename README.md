POC : Emulation of latencies and bandwidth constraints on G5K

```
vagrant up
# generate the inventory, and constraint matrix
./setup.rb
# enforce the constraints
ansible-playbook -i inventory.generated setup.yml -e @constraints.yml
# validate the constraints
ansible-playbook -i inventory.generated test.yml
```


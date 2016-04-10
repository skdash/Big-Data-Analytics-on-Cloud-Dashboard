from auto_spin_up_api_calls import *
from utils import *

###Create instance - sequence of API calls
##instance_id = launch_new_instance(instance_name, instance_specification_id, volume_name, volume_size, volume_type)
##floating_ip_id = create_new_floating_ip()
##floating_ip_addr, instance = add_floating_ip_to_instance(instance_id, floating_ip_id)
##print floating_ip_add

#Delete instance - sequence of API calls
##deleted_instance_id = delete_instance(instance_id)
##deleted_floating_ip_id = delete_unused_floating_ip(floating_ip_id)


#CREATE CLUSTER
def create_cluster(number_of_nodes, master_spec_name, slave_spec_name):

    try:
        
        nodes = number_of_nodes
        master_name = 'master'
        slave_name = 'slave'

        m_image_id = get_image_id('CentOS')
        s_image_id = get_image_id('CentOS')

        m_spec_id = get_specification_id(master_spec_name)
        print m_spec_id + '\n'

        if (slave_spec_name is not ''):
            s_spec_id = get_specification_id(slave_spec_name)
            print s_spec_id + '\n'
        else:
            s_spec_id = ''
            

        #create master
        m_inst_status, m_inst_id = launch_new_instance('master', m_image_id, m_spec_id)
        print 'status of master ' + str(m_inst_status) + '\n'
        if (m_inst_status == 200):
            m_floating_ip_id = create_new_floating_ip()
            m_floating_ip_addr, m_inst_name = add_floating_ip_to_instance(m_inst_id, m_floating_ip_id)
            live_inst_list[m_inst_name] = m_inst_id
            live_floating_ip_list[m_inst_name] = m_floating_ip_addr
            live_floating_ip_id_list[m_inst_name] = m_floating_ip_id
            nodes = nodes - 1
            print 'number of slave nodes ' + str(nodes)
        else:
            print 'Error in creating master'
            return

        #create slaves
        if (nodes > 0):

            while(nodes):
                if (m_inst_status == 200):
                    s_inst_status, s_inst_id = launch_new_instance('slave' + str(number_of_nodes - nodes), s_image_id, s_spec_id)
                    print 'status of slave' + str(number_of_nodes - nodes) + ' ' + str(s_inst_status) + '\n'
                    if (s_inst_status == 200):
                        s_floating_ip_id = create_new_floating_ip()
                        s_floating_ip_addr, s_inst_name = add_floating_ip_to_instance(s_inst_id, s_floating_ip_id)
                        live_inst_list[s_inst_name] = s_inst_id
                        live_floating_ip_list[s_inst_name] = s_floating_ip_addr
                        live_floating_ip_id_list[s_inst_name] = s_floating_ip_id
                    else:
                        print 'Error in creating slave. Slave could not be created'
                        return
                
                nodes = nodes - 1
                print 'number of slaves left ' + str(nodes) + '\n'
                
        else:
            print 'Master node set up. No slaves to create'

    except:
        print 'Error in creating VMs'


    print live_inst_list
    print '\n\r'
    print live_floating_ip_list
    print '\n\r'
    print live_floating_ip_id_list

    return



#DELETE CLUSTER
def delete_cluster(command):
    try:
        if str(command) is 'Y':
            if (len(live_inst_list) == 0):
                print 'Error ! incorrectly called delete on a empty cluster: instances do not exist'
            elif (len(live_inst_list) > 0):
                for key in live_inst_list.keys():
                    response_status = delete_instance(live_inst_list[key])
                    if (response_status == 200):
                        print 'deleting ' + key + '\n'
                    else:
                        print 'could not delete ' + key + '\n'
                live_inst_list.clear()

            if (len(live_floating_ip_list) == 0 or len(live_floating_ip_id_list) == 0):
                print 'Error ! incorrectly called delete on a empty cluster: floating ips do not exist'
            elif ((len(live_floating_ip_list) == len(live_floating_ip_id_list)) and len(live_floating_ip_id_list) > 0):
                for key in live_floating_ip_id_list.keys():
                    response_status = delete_unused_floating_ip(live_floating_ip_id_list[key])
                    if (response_status == 200):
                        print 'deleting ip address of ' + key + '\n'
                    else:
                        print 'could not delete ip address of ' + key + '\n'
                live_floating_ip_list.clear()
                live_floating_ip_id_list.clear()
        else:
            print 'You entered no! Could not delete the cluster'
            return

    except:
        print 'Erro ! Unexpected error in delete cluster'

                     
                    
            
            
            
            
        
    


        


        
        
        

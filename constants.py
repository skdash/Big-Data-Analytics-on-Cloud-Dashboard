#Constants to be used at various places
#Includes specific id numbers of project, images, network, security group,
#security keys, volumes
#the url to call the transcirrus apis, headers to pass

base_url = 'http://transcirrus-1.oscar.priv:6969/v1.0/'
headers = {'Accept' : 'application/json' , 'username' : 'admin_team7' , 'password' : 'team7rocks'}
project_id = '2aad80ab68d041649d1823ce024c85de'
hortonworks_image_id = '644d6b91-c831-43f1-80ab-976e38fad506'


#default public network id registered with openstack neutron - use carefully
network_id = 'b3bb7b4c-d65a-422b-858e-a14af9800963'
network_name = 'network_team7'

security_group_name = 'secgroup_team7'
security_group_id = ''

security_key_name = 'seckey_team7_6761'
security_key_id = ''

#these are total volume ids used between all teams - use carefully
total_spindle_volume_id = '2b0bac8f-e96d-4e90-bef3-2fb6d8842c44'
total_ssd_volume_id = '4cab8057-cb54-4967-91b4-f2e6bd0f51f0'


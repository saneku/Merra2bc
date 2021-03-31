wrf_dir="/home/WRFV4.1.3/run_tutorial/"
wrf_input_file="wrfinput_d01"
wrf_bdy_file="wrfbdy_d01"

wrf_met_dir="/home/WPSV4.1.3/run_tutorial/"
wrf_met_files="met_em.d01.2010*"

mera_dir="/home/Merra2_data/"
mera_files="svc_MERRA2_300.inst3_3d_aer_Nv.2010*"

do_IC=True
do_BC=True

###########################################
#GOCART DUST ONLY
spc_map = [ 'DUST_1 -> 1.0*[DU001];1.e9',
            'DUST_2 -> 1.0*[DU002];1.e9',
            'DUST_3 -> 1.0*[DU003];1.e9',
            'DUST_4 -> 1.0*[DU004];1.e9',
            'DUST_5 -> 1.0*[DU005];1.e9']

#GOCART FULL
spc_map = [ 'DUST_1 -> 1.0*[DU001];1.e9',
            'DUST_2 -> 1.0*[DU002];1.e9',
            'DUST_3 -> 1.0*[DU003];1.e9',
            'DUST_4 -> 1.0*[DU004];1.e9',
            'DUST_5 -> 1.0*[DU005];1.e9',
            'SEAS_1 -> 1.0*[SS002];1.e9',
            'SEAS_2 -> 1.0*[SS003];1.e9',
            'SEAS_3 -> 1.0*[SS004];1.e9',
            'SEAS_4 -> 1.0*[SS005];1.e9',
            'so2 -> 0.453*[SO2];1.e6',
            'sulf -> 0.302*[SO4];1.e6',
            'BC1 -> 1.0*[BCPHOBIC];1.e9',
            'BC2 -> 1.0*[BCPHILIC];1.e9',
            'OC1 -> 1.0*[OCPHOBIC];1.e9', 
            'OC2 -> 1.0*[OCPHILIC];1.e9',
            'dms -> 0.467*[DMS];1.e6']
            #,'msa -> 0.302*[MSA];1.e6'

spc_map = [ 'o3 -> 0.604*[O3];1.e6','co -> 1.0*[CO];1.e6']
#spc_map = [ 'so2 -> 0.453*[SO2];1.e6','sulf -> 0.302*[SO4];1.e6']

###########################################

#CBMZ-MOSAIC_8bins SO2, Sulf, O3, CO, DUST and Sea salt (NaCl).
#oc_a0X,bc_a0X still need to be done
spc_map =['so2 -> 0.453*[SO2];1.e6',
          'o3 -> 0.604*[O3];1.e6',
          'co -> 1.0*[CO];1.e6',
          
          'oin_a01->0.01292*[DU001];1.e9',
          'oin_a02->0.03876*[DU001];1.e9',
          'oin_a03->0.19382*[DU001];1.e9',
          'oin_a04->0.30103*[DU001];1.e9',
          'oin_a05->0.30103*[DU001];1.e9',
          'oin_a06->0.20412*[DU001]+0.37963*[DU002];1.e9',
          'oin_a07->0.62037*[DU002]+0.64308*[DU003];1.e9',
          'oin_a08->0.35692*[DU003]+0.73697*[DU004];1.e9',

          'na_a01->0.086245*[SS001];1.e9',
          'na_a02->0.226471*[SS001];1.e9',
          'na_a03->0.080656*[SS001]+0.109080*[SS002];1.e9',
          'na_a04->0.169416*[SS002];1.e9',
          'na_a05->0.114876*[SS002]+0.079899*[SS003];1.e9',
          'na_a06->0.248190*[SS003];1.e9',
          'na_a07->0.065283*[SS003]+0.166901*[SS004];1.e9',
          'na_a08->0.226471*[SS004]+0.000000*[SS005];1.e9',

          'cl_a01->0.133000*[SS001];1.e9',
          'cl_a02->0.349246*[SS001];1.e9',
          'cl_a03->0.124382*[SS001]+0.168214*[SS002];1.e9',
          'cl_a04->0.261260*[SS002];1.e9',
          'cl_a05->0.177153*[SS002]+0.123215*[SS003];1.e9',
          'cl_a06->0.382739*[SS003];1.e9',
          'cl_a07->0.100674*[SS003]+0.257382*[SS004];1.e9',
          'cl_a08->0.349246*[SS004]+0.000000*[SS005];1.e9',

          'so4_a01->0.057541*[SO4];1.e9',
          'so4_a02->0.116135*[SO4];1.e9',
          'so4_a03->0.264759*[SO4];1.e9',
          'so4_a04->0.246169*[SO4];1.e9',
          'so4_a05->0.091116*[SO4];1.e9',
          'so4_a06->0.013328*[SO4];1.e9',
          'so4_a07->0.000762*[SO4];1.e9',
          'so4_a08->0.000017*[SO4];1.e9',

          'num_a01->5.855e+16*[DU001]+1.147e+18*[SS001]+3.621e+17*[SO4];1',
          'num_a02->2.196e+16*[DU001]+3.766e+17*[SS001]+9.136e+16*[SO4];1',
          'num_a03->1.372e+16*[DU001]+1.676e+16*[SS001]+2.267e+16*[SS002]+2.604e+16*[SO4];1',
          'num_a04->2.664e+15*[DU001]+4.401e+15*[SS002]+3.026e+15*[SO4];1',
          'num_a05->3.330e+14*[DU001]+3.731e+14*[SS002]+2.595e+14*[SS003]+1.400e+14*[SO4];1',
          'num_a06->2.663e+13*[DU001]+4.953e+13*[DU002]+1.008e+14*[SS003]+2.560e+12*[SO4];1',
          'num_a07->1.012e+13*[DU002]+1.049e+13*[DU003]+3.313e+12*[SS003]+8.469e+12*[SS004]+1.829e+10*[SO4];1',
          'num_a08->7.276e+11*[DU003]+1.502e+12*[DU004]+1.436e+12*[SS004]+1.599e-03*[SS005]+5.048e+07*[SO4];1']

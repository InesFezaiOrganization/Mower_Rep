def get_dimensions(f_Tondeuse):
    """ Recuperate the lawn dimensions from Tondeuse.txt.
    
    Parameters
    ----------
    f_Tondeuse (string): Tondeuse file's contents. 
  
    Returns
    ----------
    int: The value of espace_i which is the length of the axis I.
    int: The value of espace_j which is the length of the axis J.
    
    """
    
    espace_i=int(f_Tondeuse[0][0:1])
    espace_j=int(f_Tondeuse[0][1:2])
    
    if espace_i<0 or espace_j<0:
        raise NotImplementedError("lawn surface dimensions are negative !")
    return espace_i,espace_j


def get_initial_position_direction(f_pos_dir):
    """ Recuperate the initial position and direction of a mower.
    
    Parameters
    ----------
    f_pos_dir (string): Tondeuse file's line containing iformations about the initial position and direction of a mower . 
  
    Returns
    ----------
    int: The initial position of a mower on the axis I.
    int: The initial position of a mower on the axis J.
    string: The initial direction of a mower
    
    """
    espace_i=int(f_pos_dir[0:1])
    espace_j=int(f_pos_dir[1:2])
    direction=f_pos_dir.split(' ',2)[1]
    
    if espace_i<0 or espace_j<0:
        raise NotImplementedError("Mower initial positions are negative !")
    return espace_i,espace_j, direction




def main():
    path_tondeuse="Tondeuse.txt"

    f_Tondeuse=open(path_tondeuse, "r")
    f_Tondeuse=f_Tondeuse.readlines()
    espace_i,espace_j=get_dimensions(f_Tondeuse)
    
    for i in range(1,int((len(f_Tondeuse)+1)/2)):
        current_i,current_j,current_direction= get_initial_position_direction(f_Tondeuse[2*i-1])
    

    

if __name__ == "__main__":
    main()

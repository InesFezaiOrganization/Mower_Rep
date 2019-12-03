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




def main():
    path_tondeuse="Tondeuse.txt"

    f_Tondeuse=open(path_tondeuse, "r")
    f_Tondeuse=f_Tondeuse.readlines()
    espace_i,espace_j=get_dimensions(f_Tondeuse)
    

    

if __name__ == "__main__":
    main()

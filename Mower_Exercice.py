import regex

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


def To_advance(current_i,current_j,current_direction,espace_i,espace_j):
    """ Updates the current positions after verifying tha the mower dosn't exceed the the lawn surface.
    
    Parameters
    ----------
    current_i (int): The current position of the mower on the axis I.
    current_j (int): The current position of the mower on the axis J.
    current_direction (string): The current direction of the mower.
    espace_i (int): The length of the axis I.
    espace_j (int): The length of the axis J.
    
    Returns
    ----------
    int: The updated current position of a mower on the axis I.
    int: The updated current position of a mower on the axis J.
    
    """
    if current_direction=="N" and current_j+1<=espace_j:
        current_j+=1
    elif current_direction=="S" and current_j-1>=0:
        current_j-=1
    elif current_direction=="E" and current_i+1<=espace_i:
        current_i+=1
    elif current_direction=="W" and current_j-1>=0:
        current_i-=1
    
    return current_i,current_j

def Manage_direction(current_direction,i):
    """ Updates the current direction of a mower.
    
    Parameters
    ----------
    current_direction (string): The current direction of the mower.
    
    Returns
    ----------
    string: The updated current direction of a mower.
    
    """
    dict_G={"N": "W", "S": "E", "E": "N", "W": "S"} 
    dict_D={"N": "E", "S": "W", "W": "N", "E":"S"}
    if i=="G":
        current_direction=dict_G[current_direction]
    else:
        current_direction=dict_D[current_direction]
    
    return current_direction


def To_move(instructions,current_i,current_j,current_direction,espace_i,espace_j):
    """ Manage the flow of a mower's instructions.
    
    Parameters
    ----------
    instructions (string): The string containing instructions.
    current_i (int): The current position of the mower on the axis I.
    current_j (int): The current position of the mower on the axis J.
    current_direction (string): The current direction of the mower.
    espace_i (int): The length of the axis I.
    espace_j (int): The length of the axis J.
    
    Returns
    ----------
    int: The updated current position of the mower on the axis I.
    int: The updated current position of the mower on the axis J.
    string: The updated current direction of a mower.
    
    """
    for i in instructions:
        if i=="A":
            current_i,current_j=To_advance(current_i,current_j,current_direction,espace_i,espace_j)
        else :
            current_direction=Manage_direction(current_direction,i)
            
    return current_i,current_j,current_direction





def main():
    path_tondeuse="Tondeuse.txt"

    f_Tondeuse=open(path_tondeuse, "r")
    f_Tondeuse=f_Tondeuse.readlines()
    espace_i,espace_j=get_dimensions(f_Tondeuse)
    
    for i in range(1,int((len(f_Tondeuse)+1)/2)):
        current_i,current_j,current_direction= get_initial_position_direction(f_Tondeuse[2*i-1])
        instructions=regex.sub(r"[^A-Za-z]+", '', f_Tondeuse[2*i])
        print("Mower number ",i,"has this coordinates: ",To_move(instructions,current_i,current_j,current_direction,espace_i,espace_j))

    

    

if __name__ == "__main__":
    main()

import os
import zhaires
from zhaires import run_directory
from os.path import join, dirname
from typing import Optional


def create_shower(name: str,
                  particle: str,
                  energy: float,
                  zenith: float,
                  azimuth: float,
                  lat: float,
                  lon: float,
                  ground: float = 0.,
                  thinning: float = 1e-6,
                  injection: float = 100.,
                  restart: bool = False,
                  default: Optional[str] = None,
                  program: Optional[str] = None,
                  **kwargs) -> zhaires.Task:
    """
    Create a new ZHAireS task with the given event parameters.

    Parameters
    ----------
    name: str
        The name of the simulation.
    particle: str
        The ZHAireS string identifying the primary particle type ('proton')
    energy: float
        The cosmic ray energy in log10(eV).
    zenith: float
        The zenith angle of the shower axis in degrees.
    azimuth: float
        The geographic azimuth angle of the shower axis in degrees.
    lat: float
        The latitude of the shower access intersecting the ground in degrees.
    lon: float
        The longitude of the shower access intersecting the ground in degrees.
    ground: float
        The ground altitude at the event location in km.
    thinning: float
        The relative thinning level for the simulation (default: 1e-6).
    injection: float
        The injection altitude (in km).
    restart: bool
        If True, don't error if the simulation already exists/already started.
    default: Optional[str]
        The path to a default Aires input file to load before other commands.
    program: Optional[str]
        The path to the ZHAires binary used to create this simulation.


    Returns
    -------
    sim: zhaires.Task
        The created ZHAires simulation that can be run with `sim.run()`.
    """
    # create the simulation directory name
    directory = join(run_directory, f'{name}')

    # create the output directory
    try:
        os.makedirs(directory, exist_ok=True)
    except Exception as e:
        if restart:
            print('Simulation directory exists. Restarting...')
        else:
            print(e)
            raise ValueError('Simulation already exists. Quitting...')

    # change to the sim directory
    os.chdir(directory)

    # the common defaults file
    common_default = join(dirname(dirname(__file__)),
                          *('defaults', 'common_default.inp'))

    # create a new simulation using the ANITA defaults
    sim = zhaires.Task(program=program, cmdfile=common_default)

    # and load any additional settings from the user provided file
    sim.load_from_file(default)

    # set the name of the task
    sim.task_name(name)

    # specify the output directory
    sim.file_directory(directory, 'All')

    # setup the primary particle energy
    sim.primary_particle(particle)
    sim.primary_energy(10.**energy)

    # and the zenith and azimuth information
    sim.primary_zenith(zenith)
    sim.primary_azimuth(azimuth)

    # create the site for this event
    sim.add_site('LatLonAltSite', lat, lon, 1e3 * ground, unit='m')

    # and enable this site for the simulation
    sim.site('LatLonAltSite')

    # setup the thinning
    sim.thinning_energy(thinning, relative=True)

    # set the injection altitude
    sim.injection_altitude(injection)

    # and return the simulation
    return sim


def create_reflected(*args, **kwargs) -> zhaires.Task:
    """
    This is a wrapper around `create_shower` that also loads
    the reflected default file. See docstring for create_shower.
    """

    # the location of the ZHAires default input file
    default = join(dirname(dirname(__file__)),
                   *('defaults', 'reflected_default.inp'))

    # if program exists, use that name
    name = 'AiresQ' if kwargs.get('model') == 'AiresQ' else 'Aires'

    # and the location of the corresponding Aires binary
    program = join(dirname(dirname(__file__)),
                   *('aires', 'aires_reflected_install', 'bin', name))

    # and then call create_shower with the given default card
    return create_shower(*args, program=program, default=default, **kwargs)


def create_direct(*args, **kwargs) -> zhaires.Task:
    """
    This is a wrapper around `create_shower` that also loads
    the direct default file. See docstring for create_shower.
    """

    # the location of the ZHAires default input file
    default = join(dirname(dirname(__file__)),
                   *('defaults', 'direct_default.inp'))

    # and the location of the corresponding Aires binary
    program = join(dirname(dirname(__file__)),
                   *('aires', 'aires_direct_install', 'bin', 'Aires'))

    # and then call create_shower with the given default card
    return create_shower(*args, program=program, default=default, **kwargs)


def create_stratospheric(name: str,
                         particle: str,
                         energy: float,
                         zenith: float,
                         azimuth: float,
                         lat: float,
                         lon: float,
                         ground: float = 0.,
                         height: float = 38.,
                         thinning: float = 1e-6,
                         restart: bool = False,
                         **kwargs) -> zhaires.Task:
    """
    Create a new ZHAireS simulation of a reflected CR event
    with a given set of parameters.

    Parameters
    ----------
    name: str
        The name of the simulation.
    particle: str
        The ZHAireS string identifying the primary particle type.
    energy: float
        The cosmic ray energy in log10(eV).
    zenith: float
        The zenith angle of the shower axis in degrees.
    azimuth: float
        The geographic azimuth angle of the shower axis in degrees.
    lat: float
        The latitude of the shower access intersecting the ground in degrees.
    lon: float
        The longitude of the shower access intersecting the ground in degrees.
    ground: float
        The ground altitude at the event location in km.
    height: float
        The height (in km) that the trajectory crosses the z-axis.
    thinning: float
        The relative thinning level for the simulation (default: 1e-6).
    restart: bool
        If True, attempt to restart a simulation with the same name.

    Returns
    -------
    sim: zhaires.Task
        The created ZHAires simulation that can be run with `sim.run()`.
    """

    # the location of the ZHAires default input file
    default = join(dirname(dirname(__file__)),
                   *('defaults', 'stratospheric_default.inp'))

    # if program exists, use that name
    pname = 'AiresQ' if kwargs.get('model') == 'AiresQ' else 'Aires'

    # the binary directory for the stratospheric ZHAireS version
    bindir = join(dirname(dirname(__file__)),
                  *('aires', 'aires_stratospheric_install', 'bin'))

    # and the location of the corresponding Aires binary
    program = join(bindir, pname)

    # create the simulation directory name
    directory = join(run_directory, f'{name}')

    # create the output directory
    try:
        os.makedirs(directory, exist_ok=True)
    except Exception as e:
        if restart:
            print('Simulation directory exists. Restarting...')
        else:
            print(e)
            raise ValueError('Simulation already exists. Quitting...')

    # change to the sim directory
    os.chdir(directory)

    # create a new simulation using the ANITA defaults
    sim = zhaires.Task(program=program, cmdfile=default)

    # the common defaults file
    common_default = join(dirname(dirname(__file__)),
                          *('defaults', 'common_default.inp'))

    # create a new simulation using the ANITA defaults
    sim = zhaires.Task(program=program, cmdfile=common_default)

    # and load any additional settings from the user provided file
    sim.load_from_file(default)

    # set the name of the task
    sim.task_name(name)

    # specify the output directory
    sim.file_directory(directory, 'All')

    # we must specify the path to the RASPASS binary
    # that creates the special particles
    raspass = join(bindir, 'RASPASSprimary')

    # and create the three special primary definitions
    for particle in ["Proton", "Iron", "Electron"]:
        sim(f"AddSpecialParticle RASPASS{particle} {raspass} {particle}")

    # get the name of RASSPAS primary
    if particle.lower() == 'proton':
        special = "RASPASSProton"
    elif particle.lower() == 'iron':
        special = "RASPASSIron"
    elif particle.lower() == 'electron':
        special = "RASPASSElectron"
    else:
        msg = (f"stratospheric showers are only supported "
               "for 'proton', 'iron', and 'electron' primaries.")
        raise ValueError(msg)

    # setup the primary particle energy to be the special RASPASS particle
    sim.primary_particle(special)
    sim.primary_energy(10.**energy)

    # and the zenith and azimuth information - for stratospheric,
    # we take the complement of the zenith
    sim.primary_zenith(180. - zenith)
    sim.primary_azimuth(azimuth)

    # create the site for this event
    sim.add_site('LatLonAltSite', lat, lon, 1e3 * ground, unit='m')

    # and enable this site for the simulation
    sim.site('LatLonAltSite')

    # setup the thinning
    sim.thinning_energy(thinning, relative=True)

    # and set the height at which the particle cross the z-axis
    sim.read_cmd(f"SetGlobal RASPASSHeight {height*1e3:.2f}")

    # and return the simulation
    return sim,


# and set the appropriate docstrings
create_direct.__doc__ = create_shower.__doc__
create_reflected.__doc__ = create_shower.__doc__

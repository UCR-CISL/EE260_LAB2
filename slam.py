class SLAM:
    def __init__(self):
        # Setup Sensors:
        self.sensors()

        # Add other initialization logic here
        pass

    def sensors(self):  # pylint: disable=no-self-use
        """
        Define the sensor suite required by the detector. The location is defined with respect to the actor center
        -- x axis is longitudinal (forward-backward)
        -- y axis is lateral (left and right)
        -- z axis is vertical
        Unit is in meters

        :return: a list containing the required sensors in the following format:

        [
            {'type': 'sensor.camera.rgb', 'x': 0.7, 'y': -0.4, 'z': 1.60, 'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0,
                      'width': 300, 'height': 200, 'fov': 100, 'id': 'Left'},

            {'type': 'sensor.camera.rgb', 'x': 0.7, 'y': 0.4, 'z': 1.60, 'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0,
                      'width': 300, 'height': 200, 'fov': 100, 'id': 'Right'},

            {'type': 'sensor.lidar.ray_cast', 'x': 0.7, 'y': 0.0, 'z': 1.60, 'yaw': 0.0, 'pitch': 0.0, 'roll': 0.0,
             'id': 'LIDAR'}
        ]

        """
        sensors = [
            {'type': 'sensor.camera.rgb', 'x': 0.7, 'y': -0.4, 'z': 1.60, 'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0,
                      'width': 1280, 'height': 720, 'fov': 100, 'id': 'Left'},

            {'type': 'sensor.camera.rgb', 'x': 0.7, 'y': 0.4, 'z': 1.60, 'roll': 0.0, 'pitch': 0.0, 'yaw': 0.0,
                      'width': 1280, 'height': 720, 'fov': 100, 'id': 'Right'},

            {'type': 'sensor.lidar.ray_cast', 'x': 0.7, 'y': 0.0, 'z': 1.60, 'yaw': 0.0, 'pitch': 0.0, 'roll': 0.0,
                      'range': 50, 
                      'rotation_frequency': 20, 'channels': 64,
                      'upper_fov': 4, 'lower_fov': -20, 'points_per_second': 2304000,
                      'id': 'LIDAR'},

            {'type': 'sensor.other.gnss', 'x': 0.7, 'y': -0.4, 'z': 1.60, 'id': 'GPS'}
        ]

        return sensors

    def get_trajectory(self, sensor_data):
        """Compute trajectory using 
        """
        try:
            prev_sensor_data = sensor_data[-2]
        except:
            # On the first step, prev_sensor_data will be None
            return None
        
        return {}

    
class Metadata(object):
    """ A simple container for ND2 metadata. """
    def __init__(self, height, width, channels, date, wells, fields_of_view, frames, z_levels, total_images_per_channel, pixel_microns):
        self._height = height
        self._width = width
        self._channels = channels
        self._date = date
        self._wells = wells
        self._fields_of_view = fields_of_view
        self._frames = frames
        self._z_levels = z_levels
        self._total_images_per_channel = total_images_per_channel
        self._pixel_microns = pixel_microns

    @property
    def height(self):
        """
        The image height in pixels.

        :rtype: int

        """
        return self._height

    @property
    def width(self):
        """
        The image width in pixels.

        :rtype: int

        """
        return self._width

    @property
    def date(self):
        """
        The date and time when acquisition began.

        :rtype: datetime.datetime() or None

        """
        return self._date

    @property
    def channels(self):
        """
        These are labels created by the NIS Elements user. Typically they may a short description of the filter cube
        used (e.g. "bright field", "GFP", etc.)

        :rtype: list

        """
        return self._channels

    @property
    def wells(self):
        """
        These are labels assigned to wells for plate imaging, e.g. "A01", "B02", etc

        :rtype: list
        """
        return self._wells

    @property
    def fields_of_view(self):
        """
        The metadata contains information about fields of view, but it contains it even if some fields
        of view were cropped. We can't find anything that states which fields of view are actually
        in the image data, so we have to calculate it. There probably is something somewhere, since
        NIS Elements can figure it out, but we haven't found it yet.

        :rtype: list

        """
        return self._fields_of_view

    @property
    def frames(self):
        """
        The number of cycles.

        :rtype:     list

        """
        return self._frames

    @property
    def z_levels(self):
        """
        The different levels in the Z-plane. Just a sequence from 0 to n.

        :rtype: list

        """
        return self._z_levels

    @property
    def total_images_per_channel(self):
        """
        The total number of images of a particular channel (wavelength, filter, etc) in the entire ND2.

        :rtype:    int

        """
        return self._total_images_per_channel

    @property
    def pixel_microns(self):
        """
        The width of a pixel in microns.

        :rtype:     float

        """
        return self._pixel_microns

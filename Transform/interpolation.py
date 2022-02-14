class interpolation:

    def linear_interpolation(self,left,right,x,):
        """Computes the linear interpolation at location pti using pt1 and pt2 as input.
        1. Please change the function definition to add the the required arguments as needed.
        2. This function performs linear interpolation between two one dimensional points and returns the interpolated value.        
        This function will require the following values
        pt1: Location of point pt1 (z1)
        I1: Intensity at the location pt1
        pt2: Location of point pt2 (z2)
        I2: Intensity at the location pt2
        pti: Location at which to detemine the interploated value (z)
        return Ii or interploated intentity at location pti"""

        I=left[2]+(right[2]-left[2])*((x-left[0])/right[0]-left[0])
        return  I

    def bilinear_interpolation(self,p1, p2, p3, p4, unknown):
        """Computes the bilinear interpolation at location pti using pt1, pt2, pt3, and pt4 as input
        1. Please change the function definition to add the the required arguments as needed.
        2. This function performs bilinear interpolation between four two dimensional points and returns the interpolated value.        
        3. This is accomplished by performing linear interpolation three times. Reuse or call linear interpolation method above to compute this task.
        This function will require the following values
        pt1: Location of the point pt1 (x1, y1)
        I1: Intensity at location pt1
        pt2: Location of the point pt2 (x2, y2)
        I2: Intensity at location pt2
        pt3: Location of the point pt3 (x3, y3)
        I3: Intensity at location pt3
        pt4: Location of the point pt4 (x4, y4)
        I4: Intensity at location pt4
        pti: Location at which to detemine the interploated value (x, y)
        return Ii or interploated intentity at location pti"""

        x = round(unknown[0])
        y=  p1[1]
        l1= interpolation.linear_interpolation(self,p1, p3,x)
        x1 = round(unknown[0])
        y1 = p2[1]
        l2 = interpolation.linear_interpolation(self,p2, p4, x1)
        test1 = (x,y,l1)
        test2=(x1,y1,l2)
        ori= interpolation.linear_interpolation(self,test1, test2, unknown[0])

        return ori

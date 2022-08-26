class interpolation:

    def linear_interpolation(self,left,right,x,):
 
        I=left[2]+(right[2]-left[2])*((x-left[0])/right[0]-left[0])
        return  I

    def bilinear_interpolation(self,p1, p2, p3, p4, unknown):


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

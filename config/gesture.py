############################################################################
#### Code Generation ####
############################################################################
#GESTURE 
if (getDeviceName.getDefaultValue() in ["SAME51","SAME53","SAME54","SAMD51"]):
    # Library File
    gestureLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_GESTURE_LIB", None)
    gestureLibraryFile.setSourcePath("/src/libraries/0x0023_qtm_surface_gestures_cm4.X.a")
    gestureLibraryFile.setOutputName("0x0023_qtm_surface_gestures_cm4.X.a")
    gestureLibraryFile.setDestPath("/touch/lib/")
    gestureLibraryFile.setEnabled(False)
elif (getDeviceName.getDefaultValue() in ["SAML10","SAML11"]):
    # Library File
    gestureLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_GESTURE_LIB", None)
    gestureLibraryFile.setSourcePath("/src/libraries/0x0023_qtm_surface_gestures_cm23.X.a")
    gestureLibraryFile.setOutputName("0x0023_qtm_surface_gestures_cm23.X.a")
    gestureLibraryFile.setDestPath("/touch/lib/")
    gestureLibraryFile.setEnabled(False)
else:
    # Library File
    gestureLibraryFile = qtouchComponent.createLibrarySymbol("TOUCH_GESTURE_LIB", None)
    gestureLibraryFile.setSourcePath("/src/libraries/0x0023_qtm_surface_gestures_cm0p.X.a")
    gestureLibraryFile.setOutputName("0x0023_qtm_surface_gestures_cm0p.X.a")
    gestureLibraryFile.setDestPath("/touch/lib/")
    gestureLibraryFile.setEnabled(False)
# Header File
gestureHeaderFile = qtouchComponent.createFileSymbol("TOUCH_GESTURE_HEADER", None)
gestureHeaderFile.setSourcePath("/src/qtm_gestures_2d_0x0023_api.h")
gestureHeaderFile.setOutputName("qtm_gestures_2d_0x0023_api.h")
gestureHeaderFile.setDestPath("/touch/")
gestureHeaderFile.setProjectPath("config/" + configName + "/touch/")
gestureHeaderFile.setType("HEADER")
gestureHeaderFile.setMarkup(False)
gestureHeaderFile.setEnabled(False)

################################################################################
#### Components ####
################################################################################

gestureMenu = qtouchComponent.createMenuSymbol("GESTURE_MENU", enableGestureMenu)
gestureMenu.setLabel("Gesture Configuration")

#Gesture Parameters
#Tap
tapMenu = qtouchComponent.createMenuSymbol("TAP_MENU", enableGestureMenu)
tapMenu.setLabel("Tap Configuration")

tapRelTimeout = qtouchComponent.createIntegerSymbol("TAP_RELEASE_TIMEOUT", tapMenu)
tapRelTimeout.setLabel("Tap Release timeout")
tapRelTimeout.setDefaultValue(20)
tapRelTimeout.setMin(3)
tapRelTimeout.setMax(255)
tapRelTimeout.setDescription("The TAP_RELEASE_TIMEOUT parameter limits the amount of time allowed between the initial finger press and the liftoff.Exceeding this value will cause the firmware to not consider the gesture as a tap gesture. TAP_RELEASE_TIMEOUT should be lesser than the TAP_HOLD_TIMEOUT and SWIPE_TIMEOUT.Unit: x10 ms. Example: if TAP_RELEASE_TIMEOUT is configured as 3, then the user should finish tapping within 30 ms to qualify the gesture as tap.")

tapHoldTimeout = qtouchComponent.createIntegerSymbol("TAP_HOLD_TIMEOUT", tapMenu)
tapHoldTimeout.setLabel("Tap Hold timeout")
tapHoldTimeout.setDefaultValue(100)
tapHoldTimeout.setMin(0)
tapHoldTimeout.setMax(255)
tapHoldTimeout.setDescription("If a finger stays within the bounds set by TAP_AREA and is not removed, the firmware will report a Tap Hold gesture once the gesture timer exceeds the TAP_HOLD_TIMEOUT value.HOLD_TAP is a single finger gesture whereas HOLD_TAP_DUAL is dual finger gesture. Ideally, TAP_HOLD_TIMEOUT should be greater than the TAP_RELEASE_TIMEOUT and SWIPE_TIMEOUT. Unit: x10 ms. Example: if TAP_HOLD_TIMEOUT is configured as 6, then the user should tap and hold inside the TAP_AREA for 60 ms to qualify the gesture as tap and hold.")

tapArea= qtouchComponent.createIntegerSymbol("TAP_AREA", tapMenu)
tapArea.setLabel("Tap Area")
tapArea.setDefaultValue(20)
tapArea.setMin(0)
tapArea.setMax(255)
tapArea.setDescription("The TAP_AREA bounds the finger to an area it must stay within to be considered a tap gesture when the finger is removed and tap and hold gesture if the finger is not removed for sometime.Unit: coordinates.Example: if TAP_AREA is configured as 20, then user should tap within 20 coordinates to detect the tap gesture.")

seqTapDistanceThreshold= qtouchComponent.createIntegerSymbol("DISTANCE_THRESHOLD", tapMenu)
seqTapDistanceThreshold.setLabel("Seq Tap distance threshold")
seqTapDistanceThreshold.setDefaultValue(50)
seqTapDistanceThreshold.setMin(0)
seqTapDistanceThreshold.setMax(255)
seqTapDistanceThreshold.setDescription("The SEQ_TAP_DIST_THRESHOLD parameter limits the allowable distance of the current touch's initial press from the liftoff position of the previous touch.It is used for multiple taps (double-tap, triple-tap etc).If the taps following the first are within this threshold, then the tap counter will be incremented.If the following tap gestures exceed this threshold, the previous touch is sent as a single tap and the current touch will reset the tap counter.Unit: coordinates.Example: if SEQ_TAP_DIST_THRESHOLD is configured as 20, after the first tap, if the user taps again within 20 coordinates, it is considered as double tap gesture.")

#Swipe
swipeMenu = qtouchComponent.createMenuSymbol("SWIPE_MENU", enableGestureMenu)
swipeMenu.setLabel("Swipe Configuration")

edgeBoundary= qtouchComponent.createIntegerSymbol("EDGE_BOUNDARY", swipeMenu)
edgeBoundary.setLabel("Edge Boundary")
edgeBoundary.setDefaultValue(0)
edgeBoundary.setMin(0)
edgeBoundary.setMax(255)
edgeBoundary.setDescription("The firmware can also be modified to define an edge region along the border of the touch sensor.With Edge Boundary defined, swipe gestures that start in an edge region will be reported as edge swipe gestures in place of normal swipe gestures.To create an edge region, the EDGE_BOUNDARY is set with the size (in touch coordinates) of the edge region.Unit: coordinates.Example: Setting the EDGE_BOUNDARY parameter to 100 will designate the area 100 units in from each edge as the edge region.")

swipeTimeout= qtouchComponent.createIntegerSymbol("SWIPE_TIMEOUT", swipeMenu)
swipeTimeout.setLabel("Swipe Timeout")
swipeTimeout.setDefaultValue(70)
swipeTimeout.setMin(0)
swipeTimeout.setMax(255)
swipeTimeout.setDescription("The SWIPE_TIMEOUT limits the amount of time allowed for the swipe gesture (initial finger press, moving in a particular direction crossing the distance threshold and the liftoff).Ideally, SWIPE_TIMEOUT should be greater than TAP_RELEASE_TIMEOUT but smaller than the TAP_HOLD_TIMEOUT.Unit: x10 ms.Example: if SWIPE_TIMEOUT is configured as 5, then the user should swipe in a particular direction and liftoff within 50 ms to qualify the gesture as swipe.")
horiSwipeDistanceThreshold= qtouchComponent.createIntegerSymbol("HORIZONTAL_SWIPE_DISTANCE_THRESHOLD", swipeMenu)
horiSwipeDistanceThreshold.setLabel("Horizontal Swipe distance threshold")
horiSwipeDistanceThreshold.setDefaultValue(30)
horiSwipeDistanceThreshold.setMin(0)
horiSwipeDistanceThreshold.setMax(255)
horiSwipeDistanceThreshold.setDescription("HORIZONTAL_SWIPE_DISTANCE_THRESHOLD controls the distance travelled in the X axis direction for detecting Left and Right Swipe gestures.Unit: X-coordinate.Example: If HORIZONTAL_SWIPE_DISTANCE_THRESHOLD is configured as 50, and a user places their finger at x-coordinate 100, they must move to at least x-coordinate 50 to record a left swipe gesture.")

vertSwipeDistanceThreshold= qtouchComponent.createIntegerSymbol("VERTICAL_SWIPE_DISTANCE_THRESHOLD", swipeMenu)
vertSwipeDistanceThreshold.setLabel("Vertical swipe distance threshold")
vertSwipeDistanceThreshold.setDefaultValue(40)
vertSwipeDistanceThreshold.setMin(0)
vertSwipeDistanceThreshold.setMax(255)
vertSwipeDistanceThreshold.setDescription("VERTICAL_SWIPE_DISTANCE_THRESHOLD controls the distance travelled in the Y axis direction for detecting Up and Down Swipe gestures.Unit: Y-coordinate.Example: if VERTICAL_SWIPE_DISTANCE_THRESHOLD is configured as 30, and a user places their finger at y-coordinate 100, they must move to at least y-coordinate 70 to record a down swipe gesture.")

#Wheel
wheelMenu = qtouchComponent.createMenuSymbol("WHEEL_MENU", enableGestureMenu)
wheelMenu.setLabel("Wheel Configuration")

wheelPostScaler= qtouchComponent.createIntegerSymbol("WHEEL_POSTSCALER", wheelMenu)
wheelPostScaler.setLabel("Wheel Post-scaler")
wheelPostScaler.setDefaultValue(1)
wheelPostScaler.setMin(0)
wheelPostScaler.setMax(255)
wheelPostScaler.setDescription("The clockwise wheel is performed with 4 swipes (right->down->left->up). Similarly, the anti-clockwise wheel is performed with 4 swipes (left->down->right->up).To detect a wheel, the minimum number of swipe required is wheel start quadrant count + wheel post scaler.Once the wheel is detected, for post scaler number of swipe detections, the wheel counter will be incremented by 1.Example: if wheel post scaler is 2, then for each two swipe detection, the wheel counter will be incremented by 1.")

wheelStartQuadrantCount= qtouchComponent.createIntegerSymbol("WHEEL_START_QUADRANT_COUNT", wheelMenu)
wheelStartQuadrantCount.setLabel("Wheel Start Quadrant count")
wheelStartQuadrantCount.setDefaultValue(2)
wheelStartQuadrantCount.setMin(2)
wheelStartQuadrantCount.setMax(255)
wheelStartQuadrantCount.setDescription("The wheel gesture movement can be broken down into 90 degree arcs.The firmware watches for a certain number of arcs to occur in a circular pattern before starting to report wheel gesture information.The number of arcs that must be first detected is determined by the WHEEL_START_QUADRANT_COUNT parameter.Lower values for this parameter make it faster to start a wheel gesture, but it also makes the firmware prone to prematurely reporting wheel gesture information.Example: if WHEEL_START_QUADRANT_COUNT is configured as 2, then after 180 degree, the gesture is updated as Wheel.")

wheelReverseQuadrantCount= qtouchComponent.createIntegerSymbol("WHEEL_REVERSE_QUADRANT_COUNT", wheelMenu)
wheelReverseQuadrantCount.setLabel("Wheel Reverse Quadrant count")
wheelReverseQuadrantCount.setDefaultValue(2)
wheelReverseQuadrantCount.setMin(2)
wheelReverseQuadrantCount.setMax(255)
wheelReverseQuadrantCount.setDescription("The WHEEL_REVERSE_QUADRANT_COUNT performs a similar function as WHEEL_START_QUADRANT_COUNT except it is used when changing the direction of the wheel instead of starting it new.This is used to prevent quick toggling between directions.Example: If WHEEL_REVERSE_QUADRANT_COUNT is set as 4 and after some wheel gestures, if the user changes the direction of rotation, then only after 360 degree, it will be detected as one wheel gesture.")
#Pinch and Zoom
pinchZoomMenu = qtouchComponent.createMenuSymbol("PINCH_ZOOM_MENU", enableGestureMenu)
pinchZoomMenu.setLabel("Pinch and Zoom Configuration")

pinchZoomThreshold= qtouchComponent.createIntegerSymbol("PINCH_ZOOM_THRESHOLD", pinchZoomMenu)
pinchZoomThreshold.setLabel("Pinch Zoom Threshold")
pinchZoomThreshold.setDefaultValue(150)
pinchZoomThreshold.setMin(0)
pinchZoomThreshold.setMax(255)
pinchZoomThreshold.setDescription("The PINCH_ZOOM_THRESHOLD limits the allowable distance between the two fingers to detect the pinch and the zoom gestures.After crossing the PINCH_ZOOM_THRESHOLD, if the distance between the contacts is reducing, then the gesture is reported as 'PINCH'.After crossing the PINCH_ZOOM_THRESHOLD, if the distance between the contacts is increasing, then the gesture is reported as 'ZOOM'.Unit: coordinates.Example: if PINCH_ZOOM_THRESHOLD is configured as 20, then after crossing 20 coordinates, it will be reported as the pinch gesture or the zoom gesture.")


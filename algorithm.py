import cv2


def match(image_path1, image_path2, n_matches=10):
    # Load two images
    img1 = cv2.imread(image_path1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(image_path2, cv2.IMREAD_GRAYSCALE)

    # Keypoint Detection
    detector = cv2.ORB_create()
    keypoints1, descriptors1 = detector.detectAndCompute(img1, None)
    keypoints2, descriptors2 = detector.detectAndCompute(img2, None)

    # Keypoint Matching
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptors1, descriptors2)

    # Sort the matches based on their distances
    # (distances between the descriptors of the matched keypoints)
    matches = sorted(matches, key=lambda x: x.distance)

    # Set the color for matches (brighter: green)
    match_color = (0, 255, 0)

    # Set the line thickness (make it thicker)
    line_thickness = 3

    # Draw the matches with a thicker line

    # The matchesThickness argument may cause a warning.
    # This warning can be safely ignored, as it does not impact the functionality.
    return cv2.drawMatches(
        img1, keypoints1, img2, keypoints2,
        matches[:n_matches], None,
        matchColor=match_color,
        singlePointColor=(255, 0, 0),  # Color of keypoints
        flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS,
        matchesThickness=line_thickness
    )

import argparse
from algorithm import match
import cv2


def main():
    parser = argparse.ArgumentParser(description='Perform Sentinel-2 Image Matching.')
    parser.add_argument('--path1', type=str, required=True, help='Path to first image.')
    parser.add_argument('--path2', type=str, required=True, help='Path to second image.')
    parser.add_argument('--ouput_filename', type=str, required=True,
                        help='Name of the output file, together with extension.')
    parser.add_argument('--n_matches', type=int, default=10,
                        help='Number of matches to draw. If greater than the total, '
                             'all the matches are drawn')

    args = parser.parse_args()

    image_path1 = args.path1
    image_path2 = args.path2
    ouput_filename = args.ouput_filename
    n_matches = args.n_matches

    img_matches = match(image_path1, image_path2, n_matches=n_matches)

    # Save the result to an image file
    cv2.imwrite(f'./matches/{ouput_filename}', img_matches)


if __name__ == "__main__":
    main()

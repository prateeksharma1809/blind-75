package com.oa;

import java.util.Arrays;
import java.util.Comparator;

public class ClosestPairOfPoints {

    public static long closestSquaredDistance(int[] x, int[] y) {
        int n = x.length;
        Point[] points = new Point[n];
        
        for (int i = 0; i < n; i++) {
            points[i] = new Point(x[i], y[i]);
        }
        
        Arrays.sort(points, Comparator.comparingInt(p -> p.x));
        
        return closestPair(points, 0, n - 1);
    }

    private static long closestPair(Point[] points, int left, int right) {
        if (right - left <= 3) {
            return bruteForce(points, left, right);
        }

        int mid = left + (right - left) / 2;
        long d = Math.min(closestPair(points, left, mid), closestPair(points, mid + 1, right));

        Point[] strip = new Point[right - left + 1];
        int j = 0;
        for (int i = left; i <= right; i++) {
            if (Math.abs(points[i].x - points[mid].x) < d) {
                strip[j++] = points[i];
            }
        }
        
        Arrays.sort(strip, 0, j, Comparator.comparingInt(p -> p.y));
        
        return Math.min(d, stripClosest(strip, j, d));
    }

    private static long stripClosest(Point[] strip, int size, long d) {
        long min = d;
        
        for (int i = 0; i < size; ++i) {
            for (int j = i + 1; j < size && (strip[j].y - strip[i].y) * (strip[j].y - strip[i].y) < min; ++j) {
                long dist = dist(strip[i], strip[j]);
                if (dist < min) {
                    min = dist;
                }
            }
        }
        
        return min;
    }

    private static long bruteForce(Point[] points, int left, int right) {
        long min = Long.MAX_VALUE;
        for (int i = left; i < right; i++) {
            for (int j = i + 1; j <= right; j++) {
                long dist = dist(points[i], points[j]);
                if (dist < min) {
                    min = dist;
                }
            }
        }
        return min;
    }

    private static long dist(Point p1, Point p2) {
        return (long)(p1.x - p2.x) * (p1.x - p2.x) + (long)(p1.y - p2.y) * (p1.y - p2.y);
    }

    static class Point {
        int x, y;
        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) {
        int[] x = {0, 10, 15};
        int[] y = {0, 10, 20};

        System.out.println(closestSquaredDistance(x, y)); // Output: 125
    }
}

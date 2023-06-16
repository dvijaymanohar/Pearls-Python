#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This module implements the gRPC client for the ADAC (ADC + DAC) server.

   @Author: V.M. Dogiparthi <v.m.dogiparthi@tudelft.com>
   @Date: 07 Mar 2023

   Usage: python3 adac_remote_client.py
"""


# Import necessary gRPC modules
import grpc
import calibration_pb2
import calibration_pb2_grpc


def run():
    # Create a gRPC channel to connect to the server
    #with grpc.insecure_channel('192.168.1.100:50051') as channel:
    with grpc.insecure_channel('172.16.159.131:50054') as channel:

        # Create a stub for the gRPC service
        stub = calibration_pb2_grpc.CalibrationStub(
            channel)

        # Call the SetDacVoltage method on the gRPC service
        response = stub.boost_intensity_calibration(
            calibration_pb2.BoostIntensityCalibrationRequest())

        # Print the response

        print(response.status)
        # print(response.status.success)
        # print(response.status.code)
        # print(response.status.reason)

        # # Call the GetAdcVoltage method on the gRPC service
        # response = stub.GetAdcVoltage(adac_remote_pb2.GetAdcVoltageRequest(
        #     adc_channel=0, verbosity_level=True))

        # # Print the response
        # print(response.status)
        # print(response.voltage)


if __name__ == '__main__':
    run()

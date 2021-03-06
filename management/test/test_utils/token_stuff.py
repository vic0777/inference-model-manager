#
# Copyright (c) 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# flake8: noqa

keys_json = """{
  "keys": [
    {
      "use": "sig",
      "kty": "RSA",
      "kid": "e5b2b3f988394aab01f05c7c0f23cb9c02a736f4",
      "alg": "RS256",
      "n": "7CZng57Wy_O1mEPrB3eFkkf_-b_sBsh4G8p310W-aa8z13Wh_oXhHabFny15ZunUnHFYSoUOjcEmD-zHyayDDcksRk1a8UVYzwOYkm9lKfXB-CvrekVyzSAtwWZl3KBM95ptm90p-4rDb-D18YME4O_I2mcmQnM_HVqAlgl0HGMTqM6gO85sVnYJGh1KN25mBRzs-oG4Pfk8KNG8IJponFEpVnbY5V4AcgUbvhlzZ3vUjRti_2PrW6RnZITpDey80ddidCX6iNxmWPNevnhGXLCbuJ38TPPdmsg_Ij2_7dysiFMxtdHomPOm2A5n9c95VhU0kEOJcKVlsnUzPsYY8Q",
      "e": "AQAB"
    }
  ]
}"""

invalid_token = "does not look like a JWT"

user_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImU1YjJiM2Y5ODgzOTRhYWIwMWYwNWM3YzBmMjNjYjljMDJhNzM2ZjQifQ.eyJpc3MiOiJodHRwOi8vMTI3LjAuMC4xOjU1NTQvZGV4Iiwic3ViIjoiQ2lOamJqMXFZVzVsTEc5MVBWQmxiM0JzWlN4a1l6MWxlR0Z0Y0d4bExHUmpQVzl5WnhJRWJHUmhjQSIsImF1ZCI6ImV4YW1wbGUtYXBwIiwiZXhwIjoxNTM4NTYwODY5LCJpYXQiOjE1Mzg0NzQ0NjksImF0X2hhc2giOiI0VlRxU1Q4Y2JUOUczWnN3SjJSYWlRIiwiZW1haWwiOiJqYW5lZG9lQGV4YW1wbGUuY29tIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImdyb3VwcyI6WyJkZWZhdWx0IiwidGVzdCJdfQ.PTynxa0D3UNzSENX22UDNTfpxHbNDA0lydLnikVFwQ8Y9JjD2aIUHVJQz356BXTBKD-YVcMj_XuRnVml3V-8gRTaKRW23bLtXNxp443Wif3iSMPsStvyKV9PTpOXpRPWQIgrH6HdwBP7NnSM1PMYYXAdDvyeFitUD1tSKvfsywvgcNL0bTSPxGE0rSFi9LYqKuQoEiXpg_r70ZR-TGZcFs4VSoXGMEAlDrtH4GX762v8nXHs8T4z4AUt2CXV2z4F2CKsPo5GlXFfXu7Wx-lhRfgXg7k2Rca8qJtGbaAXo2rtAnlRV560Fqz1BRTmTJGs4HyIyUNFDAc3xt581FMmQw"

admin_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImU1YjJiM2Y5ODgzOTRhYWIwMWYwNWM3YzBmMjNjYjljMDJhNzM2ZjQifQ.eyJpc3MiOiJodHRwOi8vMTI3LjAuMC4xOjU1NTQvZGV4Iiwic3ViIjoiQ2lOamJqMXFhVzFwTEc5MVBWQmxiM0JzWlN4a1l6MWxlR0Z0Y0d4bExHUmpQVzl5WnhJRWJHUmhjQSIsImF1ZCI6ImV4YW1wbGUtYXBwIiwiZXhwIjoxNTM4NTYwNzU5LCJpYXQiOjE1Mzg0NzQzNTksImF0X2hhc2giOiJ3WjIzTEdGVVJrUmRLOVdDeXlIV1lnIiwiZW1haWwiOiJqaW1paGVuZHJpeEBleGFtcGxlLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJncm91cHMiOlsiYWRtaW4iXX0.K9DDDulmzpsGWKfjCp1LfTJD2d-_0bB2YNFnX24jWIroMWNDGKujsLc68zSjfD-s9HTAsJ2Ha7P92_SQLyG7Y0FH2RRHWDAbmtior5ZxcYRVAB3Q5zOT1uEHXAAmqXh7IIB0E6JoI_7oDanCstyS3RkSoobn5StwHTgxb_hTuTXU3Zdq4vg7NQ15YQRIe85I83x52ga_IZsIM6PODUL0w80_3EEwOAKYwJzsdw7trswpOOcPiepUvLjUR9jO9wvq91Ua6GXkU1Gpz3lGd_av8HBJ9lGF6e5VaZH37m8xtQcEBnanPymsH00j-_PmS3ICseMCwicyDHIyJwDCVdO9ZQ"
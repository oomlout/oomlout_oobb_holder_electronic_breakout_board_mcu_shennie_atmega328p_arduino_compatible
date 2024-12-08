$fn = 50;


difference() {
	union() {
		difference() {
			union() {
				hull() {
					translate(v = [-24.5000000000, 39.5000000000, 0]) {
						cylinder(h = 3, r = 5);
					}
					translate(v = [24.5000000000, 39.5000000000, 0]) {
						cylinder(h = 3, r = 5);
					}
					translate(v = [-24.5000000000, -39.5000000000, 0]) {
						cylinder(h = 3, r = 5);
					}
					translate(v = [24.5000000000, -39.5000000000, 0]) {
						cylinder(h = 3, r = 5);
					}
				}
				translate(v = [0, 33.7500000000, 23]) {
					hull() {
						translate(v = [-24.5000000000, 5.7500000000, 0]) {
							cylinder(h = 9, r = 5);
						}
						translate(v = [24.5000000000, 5.7500000000, 0]) {
							cylinder(h = 9, r = 5);
						}
						translate(v = [-24.5000000000, -5.7500000000, 0]) {
							cylinder(h = 9, r = 5);
						}
						translate(v = [24.5000000000, -5.7500000000, 0]) {
							cylinder(h = 9, r = 5);
						}
					}
				}
				translate(v = [0, -33.7500000000, 23]) {
					hull() {
						translate(v = [-24.5000000000, 5.7500000000, 0]) {
							cylinder(h = 9, r = 5);
						}
						translate(v = [24.5000000000, 5.7500000000, 0]) {
							cylinder(h = 9, r = 5);
						}
						translate(v = [-24.5000000000, -5.7500000000, 0]) {
							cylinder(h = 9, r = 5);
						}
						translate(v = [24.5000000000, -5.7500000000, 0]) {
							cylinder(h = 9, r = 5);
						}
					}
				}
			}
			union() {
				translate(v = [-23.9600000000, 26.4600000000, 0]) {
					rotate(a = [0, 180, 0]) {
						difference() {
							union() {
								translate(v = [0, 0, -1.7000000000]) {
									cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.4000000000);
								}
								translate(v = [0, 0, -6.0000000000]) {
									cylinder(h = 6, r = 1.5000000000);
								}
								translate(v = [0, 0, -6.0000000000]) {
									cylinder(h = 6, r = 1.8000000000);
								}
								translate(v = [0, 0, -6.0000000000]) {
									cylinder(h = 6, r = 1.5000000000);
								}
							}
							union();
						}
					}
				}
				translate(v = [24, 24, 0]) {
					rotate(a = [0, 180, 0]) {
						difference() {
							union() {
								translate(v = [0, 0, -1.7000000000]) {
									cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.4000000000);
								}
								translate(v = [0, 0, -6.0000000000]) {
									cylinder(h = 6, r = 1.5000000000);
								}
								translate(v = [0, 0, -6.0000000000]) {
									cylinder(h = 6, r = 1.8000000000);
								}
								translate(v = [0, 0, -6.0000000000]) {
									cylinder(h = 6, r = 1.5000000000);
								}
							}
							union();
						}
					}
				}
				translate(v = [-19.5000000000, -26.5000000000, 0]) {
					rotate(a = [0, 180, 0]) {
						difference() {
							union() {
								translate(v = [0, 0, -1.7000000000]) {
									cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.4000000000);
								}
								translate(v = [0, 0, -6.0000000000]) {
									cylinder(h = 6, r = 1.5000000000);
								}
								translate(v = [0, 0, -6.0000000000]) {
									cylinder(h = 6, r = 1.8000000000);
								}
								translate(v = [0, 0, -6.0000000000]) {
									cylinder(h = 6, r = 1.5000000000);
								}
							}
							union();
						}
					}
				}
				translate(v = [8.5000000000, -26.5000000000, 0]) {
					rotate(a = [0, 180, 0]) {
						difference() {
							union() {
								translate(v = [0, 0, -1.7000000000]) {
									cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.4000000000);
								}
								translate(v = [0, 0, -6.0000000000]) {
									cylinder(h = 6, r = 1.5000000000);
								}
								translate(v = [0, 0, -6.0000000000]) {
									cylinder(h = 6, r = 1.8000000000);
								}
								translate(v = [0, 0, -6.0000000000]) {
									cylinder(h = 6, r = 1.5000000000);
								}
							}
							union();
						}
					}
				}
				translate(v = [15.0000000000, 37.5000000000, 0]) {
					rotate(a = [0, 180, 0]) {
						difference() {
							union() {
								translate(v = [0, 0, -32.0000000000]) {
									rotate(a = [0, 0, 0]) {
										difference() {
											union() {
												#linear_extrude(height = 2.5000000000) {
													polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
												}
											}
											union();
										}
									}
								}
								translate(v = [0, 0, -32.0000000000]) {
									rotate(a = [0, 0, 0]) {
										difference() {
											union() {
												#linear_extrude(height = 2.5000000000) {
													polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
												}
											}
											union();
										}
									}
								}
								translate(v = [0, 0, -32.0000000000]) {
									rotate(a = [0, 0, 0]) {
										difference() {
											union() {
												#linear_extrude(height = 2.5000000000) {
													polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
												}
											}
											union();
										}
									}
								}
								#translate(v = [0, 0, -1.7000000000]) {
									cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.4000000000);
								}
								#translate(v = [0, 0, -32.0000000000]) {
									cylinder(h = 32, r = 1.5000000000);
								}
								#translate(v = [0, 0, -32.0000000000]) {
									cylinder(h = 32, r = 1.8000000000);
								}
								#translate(v = [0, 0, -32.0000000000]) {
									cylinder(h = 32, r = 1.5000000000);
								}
							}
							union();
						}
					}
				}
				translate(v = [-15.0000000000, 37.5000000000, 0]) {
					rotate(a = [0, 180, 0]) {
						difference() {
							union() {
								translate(v = [0, 0, -32.0000000000]) {
									rotate(a = [0, 0, 0]) {
										difference() {
											union() {
												#linear_extrude(height = 2.5000000000) {
													polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
												}
											}
											union();
										}
									}
								}
								translate(v = [0, 0, -32.0000000000]) {
									rotate(a = [0, 0, 0]) {
										difference() {
											union() {
												#linear_extrude(height = 2.5000000000) {
													polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
												}
											}
											union();
										}
									}
								}
								translate(v = [0, 0, -32.0000000000]) {
									rotate(a = [0, 0, 0]) {
										difference() {
											union() {
												#linear_extrude(height = 2.5000000000) {
													polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
												}
											}
											union();
										}
									}
								}
								#translate(v = [0, 0, -1.7000000000]) {
									cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.4000000000);
								}
								#translate(v = [0, 0, -32.0000000000]) {
									cylinder(h = 32, r = 1.5000000000);
								}
								#translate(v = [0, 0, -32.0000000000]) {
									cylinder(h = 32, r = 1.8000000000);
								}
								#translate(v = [0, 0, -32.0000000000]) {
									cylinder(h = 32, r = 1.5000000000);
								}
							}
							union();
						}
					}
				}
				translate(v = [15.0000000000, -37.5000000000, 0]) {
					rotate(a = [0, 180, 0]) {
						difference() {
							union() {
								translate(v = [0, 0, -32.0000000000]) {
									rotate(a = [0, 0, 0]) {
										difference() {
											union() {
												#linear_extrude(height = 2.5000000000) {
													polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
												}
											}
											union();
										}
									}
								}
								translate(v = [0, 0, -32.0000000000]) {
									rotate(a = [0, 0, 0]) {
										difference() {
											union() {
												#linear_extrude(height = 2.5000000000) {
													polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
												}
											}
											union();
										}
									}
								}
								translate(v = [0, 0, -32.0000000000]) {
									rotate(a = [0, 0, 0]) {
										difference() {
											union() {
												#linear_extrude(height = 2.5000000000) {
													polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
												}
											}
											union();
										}
									}
								}
								#translate(v = [0, 0, -1.7000000000]) {
									cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.4000000000);
								}
								#translate(v = [0, 0, -32.0000000000]) {
									cylinder(h = 32, r = 1.5000000000);
								}
								#translate(v = [0, 0, -32.0000000000]) {
									cylinder(h = 32, r = 1.8000000000);
								}
								#translate(v = [0, 0, -32.0000000000]) {
									cylinder(h = 32, r = 1.5000000000);
								}
							}
							union();
						}
					}
				}
				translate(v = [-15.0000000000, -37.5000000000, 0]) {
					rotate(a = [0, 180, 0]) {
						difference() {
							union() {
								translate(v = [0, 0, -32.0000000000]) {
									rotate(a = [0, 0, 0]) {
										difference() {
											union() {
												#linear_extrude(height = 2.5000000000) {
													polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
												}
											}
											union();
										}
									}
								}
								translate(v = [0, 0, -32.0000000000]) {
									rotate(a = [0, 0, 0]) {
										difference() {
											union() {
												#linear_extrude(height = 2.5000000000) {
													polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
												}
											}
											union();
										}
									}
								}
								translate(v = [0, 0, -32.0000000000]) {
									rotate(a = [0, 0, 0]) {
										difference() {
											union() {
												#linear_extrude(height = 2.5000000000) {
													polygon(points = [[3.1735000000, 0.0000000000], [1.5867500000, 2.7483316189], [-1.5867500000, 2.7483316189], [-3.1735000000, 0.0000000000], [-1.5867500000, -2.7483316189], [1.5867500000, -2.7483316189]]);
												}
											}
											union();
										}
									}
								}
								#translate(v = [0, 0, -1.7000000000]) {
									cylinder(h = 1.7000000000, r1 = 1.5000000000, r2 = 2.4000000000);
								}
								#translate(v = [0, 0, -32.0000000000]) {
									cylinder(h = 32, r = 1.5000000000);
								}
								#translate(v = [0, 0, -32.0000000000]) {
									cylinder(h = 32, r = 1.8000000000);
								}
								#translate(v = [0, 0, -32.0000000000]) {
									cylinder(h = 32, r = 1.5000000000);
								}
							}
							union();
						}
					}
				}
				translate(v = [-22.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 3.0000000000);
				}
				translate(v = [-7.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 3.0000000000);
				}
				translate(v = [7.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 3.0000000000);
				}
				translate(v = [22.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 3.0000000000);
				}
				translate(v = [-22.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 3.0000000000);
				}
				translate(v = [-7.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 3.0000000000);
				}
				translate(v = [7.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 3.0000000000);
				}
				translate(v = [22.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 3.0000000000);
				}
				translate(v = [-22.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-15.0000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-7.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [0.0000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [7.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [15.0000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [22.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-22.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-15.0000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-7.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [0.0000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [7.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [15.0000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [22.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-22.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-15.0000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-7.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [0.0000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [7.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [15.0000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [22.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-22.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-15.0000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-7.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [0.0000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [7.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [15.0000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [22.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-22.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-15.0000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-7.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [0.0000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [7.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [15.0000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [22.5000000000, 37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-22.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-15.0000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-7.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [0.0000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [7.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [15.0000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [22.5000000000, -37.5000000000, -100.0000000000]) {
					cylinder(h = 200, r = 1.5000000000);
				}
				translate(v = [-27.5000000000, -30.0000000000, 23]) {
					cube(size = [55, 60, 4.2000000000]);
				}
				translate(v = [-20.5000000000, 14.5000000000, 23]) {
					cube(size = [10, 15, 9]);
				}
				translate(v = [-26.0000000000, 10.5000000000, 23]) {
					cube(size = [4.6000000000, 10, 9]);
				}
				translate(v = [-10.4900000000, -12.1400000000, 23]) {
					cube(size = [3.5400000000, 39.1000000000, 9]);
				}
				translate(v = [4.7500000000, -12.1400000000, 23]) {
					cube(size = [3.5400000000, 39.1000000000, 9]);
				}
				translate(v = [12.3700000000, 15.8000000000, 23]) {
					cube(size = [8.6200000000, 11.1600000000, 9]);
				}
				translate(v = [-25.7300000000, -25.2700000000, 23]) {
					cube(size = [3.5400000000, 16.2400000000, 9]);
				}
				translate(v = [-21.9200000000, -22.3000000000, 23]) {
					cube(size = [8.6200000000, 21.3200000000, 9]);
				}
				translate(v = [-10.4900000000, -24.8400000000, 23]) {
					cube(size = [6.0800000000, 8.6200000000, 9]);
				}
				translate(v = [-16.0000000000, -29.5000000000, 23]) {
					cube(size = [6, 5, 9]);
				}
				translate(v = [-2.8700000000, -27.3800000000, 23]) {
					cube(size = [8.6200000000, 11.1600000000, 9]);
				}
				translate(v = [12.3700000000, -22.3000000000, 23]) {
					cube(size = [8.6200000000, 11.1600000000, 9]);
				}
				translate(v = [22.2300000000, -25.2700000000, 23]) {
					cube(size = [3.5400000000, 21.3200000000, 9]);
				}
			}
		}
		union() {
			translate(v = [-23.9600000000, 26.4600000000, 3.0000000000]) {
				cylinder(h = 3, r = 3.0000000000);
			}
			translate(v = [24, 24, 3.0000000000]) {
				cylinder(h = 3, r = 3.0000000000);
			}
			translate(v = [-19.5000000000, -26.5000000000, 3.0000000000]) {
				cylinder(h = 3, r = 3.0000000000);
			}
			translate(v = [8.5000000000, -26.5000000000, 3.0000000000]) {
				cylinder(h = 3, r = 3.0000000000);
			}
			#translate(v = [-23.9600000000, 26.4600000000, 27.2000000000]) {
				sphere(r = 1.5000000000);
			}
			#translate(v = [24, 24, 27.2000000000]) {
				sphere(r = 1.5000000000);
			}
			#translate(v = [-19.5000000000, -26.5000000000, 27.2000000000]) {
				sphere(r = 1.5000000000);
			}
			#translate(v = [8.5000000000, -26.5000000000, 27.2000000000]) {
				sphere(r = 1.5000000000);
			}
		}
	}
	union() {
		#translate(v = [-23.9600000000, 26.4600000000, 6]) {
			rotate(a = [0, 180, 0]) {
				cylinder(h = 6, r = 1.5000000000);
			}
		}
		#translate(v = [24, 24, 6]) {
			rotate(a = [0, 180, 0]) {
				cylinder(h = 6, r = 1.5000000000);
			}
		}
		#translate(v = [-19.5000000000, -26.5000000000, 6]) {
			rotate(a = [0, 180, 0]) {
				cylinder(h = 6, r = 1.5000000000);
			}
		}
		#translate(v = [8.5000000000, -26.5000000000, 6]) {
			rotate(a = [0, 180, 0]) {
				cylinder(h = 6, r = 1.5000000000);
			}
		}
	}
}
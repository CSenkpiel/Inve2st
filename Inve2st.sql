PGDMP     8    6    	            x           inve2st    9.6.4    11.2    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false            �           1262    274526    inve2st    DATABASE     �   CREATE DATABASE inve2st WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'German_Germany.1252' LC_CTYPE = 'German_Germany.1252';
    DROP DATABASE inve2st;
             postgres    false            �           0    0    SCHEMA public    ACL     _   REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO sozio_e2s_admin_role;
                  postgres    false    4                        3079    237914    postgis 	   EXTENSION     ;   CREATE EXTENSION IF NOT EXISTS postgis WITH SCHEMA public;
    DROP EXTENSION postgis;
                  false            �           0    0    EXTENSION postgis    COMMENT     g   COMMENT ON EXTENSION postgis IS 'PostGIS geometry, geography, and raster spatial types and functions';
                       false    2            �           0    0    TABLE geography_columns    ACL     �   REVOKE ALL ON TABLE public.geography_columns FROM postgres;
GRANT SELECT ON TABLE public.geography_columns TO sozio_e2s_read_role;
GRANT ALL ON TABLE public.geography_columns TO sozio_e2s_admin_role;
            public       postgres    false    189            �           0    0    TABLE geometry_columns    ACL     �   REVOKE ALL ON TABLE public.geometry_columns FROM postgres;
GRANT SELECT ON TABLE public.geometry_columns TO sozio_e2s_read_role;
GRANT ALL ON TABLE public.geometry_columns TO sozio_e2s_admin_role;
            public       postgres    false    190            �            1259    239425    mapping_profile_region    TABLE       CREATE TABLE public.mapping_profile_region (
    c_map_profile_reg_profile_pfk character varying NOT NULL,
    c_map_profile_reg_scenario_pfk character varying NOT NULL,
    c_map_profile_reg_reference_year_pfk integer NOT NULL,
    c_map_profile_reg_profile_type_pfk character varying NOT NULL,
    c_map_profile_reg_regions_pfk character varying NOT NULL,
    c_map_profile_reg_comment character varying,
    c_map_profile_reg_last_modified date NOT NULL,
    c_map_profile_reg_editor character varying NOT NULL
);
 *   DROP TABLE public.mapping_profile_region;
       public         postgres    false            �           0    0    TABLE mapping_profile_region    COMMENT     ]   COMMENT ON TABLE public.mapping_profile_region IS 'maps regions to its different profiles ';
            public       postgres    false    202            �           0    0 ;   COLUMN mapping_profile_region.c_map_profile_reg_profile_pfk    COMMENT     u   COMMENT ON COLUMN public.mapping_profile_region.c_map_profile_reg_profile_pfk IS 'unique identifier of the profile';
            public       postgres    false    202            �           0    0 <   COLUMN mapping_profile_region.c_map_profile_reg_scenario_pfk    COMMENT     n   COMMENT ON COLUMN public.mapping_profile_region.c_map_profile_reg_scenario_pfk IS 'Description of scenario ';
            public       postgres    false    202            �           0    0 B   COLUMN mapping_profile_region.c_map_profile_reg_reference_year_pfk    COMMENT     z   COMMENT ON COLUMN public.mapping_profile_region.c_map_profile_reg_reference_year_pfk IS 'reference year for the profile';
            public       postgres    false    202            �           0    0 @   COLUMN mapping_profile_region.c_map_profile_reg_profile_type_pfk    COMMENT     v   COMMENT ON COLUMN public.mapping_profile_region.c_map_profile_reg_profile_type_pfk IS 'abbreviation of profile type';
            public       postgres    false    202            �           0    0 ;   COLUMN mapping_profile_region.c_map_profile_reg_regions_pfk    COMMENT     �   COMMENT ON COLUMN public.mapping_profile_region.c_map_profile_reg_regions_pfk IS 'refers to NUTS nomenclature (e.g. germany = DE, Baden-Würtemberg = DE1)';
            public       postgres    false    202            �           0    0    TABLE mapping_profile_region    ACL     �   GRANT ALL ON TABLE public.mapping_profile_region TO sozio_e2s_admin_role;
GRANT SELECT ON TABLE public.mapping_profile_region TO "ENTIGRIS_read_only_role";
            public       postgres    false    202            �           0    0    TABLE raster_columns    ACL     �   REVOKE ALL ON TABLE public.raster_columns FROM postgres;
GRANT SELECT ON TABLE public.raster_columns TO sozio_e2s_read_role;
GRANT ALL ON TABLE public.raster_columns TO sozio_e2s_admin_role;
            public       postgres    false    199            �           0    0    TABLE raster_overviews    ACL     �   REVOKE ALL ON TABLE public.raster_overviews FROM postgres;
GRANT SELECT ON TABLE public.raster_overviews TO sozio_e2s_read_role;
GRANT ALL ON TABLE public.raster_overviews TO sozio_e2s_admin_role;
            public       postgres    false    200            �           0    0    TABLE spatial_ref_sys    ACL     �   REVOKE ALL ON TABLE public.spatial_ref_sys FROM postgres;
GRANT SELECT ON TABLE public.spatial_ref_sys TO sozio_e2s_read_role;
GRANT ALL ON TABLE public.spatial_ref_sys TO sozio_e2s_admin_role;
            public       postgres    false    187            �            1259    239431    tb_application    TABLE     '  CREATE TABLE public.tb_application (
    c_application_pk character varying NOT NULL,
    c_application_description character varying NOT NULL,
    c_application_comment character varying,
    c_application_last_modification date NOT NULL,
    c_application_editor character varying NOT NULL
);
 "   DROP TABLE public.tb_application;
       public         sozio_e2s_admin_role    false            �           0    0 &   COLUMN tb_application.c_application_pk    COMMENT     P   COMMENT ON COLUMN public.tb_application.c_application_pk IS 'app_1, app_2, ..';
            public       sozio_e2s_admin_role    false    203            �           0    0 +   COLUMN tb_application.c_application_comment    COMMENT     [   COMMENT ON COLUMN public.tb_application.c_application_comment IS 'comment on application';
            public       sozio_e2s_admin_role    false    203            �           0    0    TABLE tb_application    ACL     D   GRANT SELECT ON TABLE public.tb_application TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    203            �            1259    239439    tb_application_characteristics    TABLE     �  CREATE TABLE public.tb_application_characteristics (
    c_technology_pfk character varying NOT NULL,
    c_investment_options_size_pk int4range NOT NULL,
    c_investment_options_units_pfk character varying NOT NULL,
    c_application_characteristics_validity_time_pk daterange NOT NULL,
    c_application_pfk character varying NOT NULL,
    c_application_characteristics_scenario_pk character varying NOT NULL,
    c_application_characteristics_regions_fk character varying NOT NULL,
    c_application_characteristic_types_pk character varying NOT NULL,
    c_application_characteristics_value double precision NOT NULL,
    c_application_characteristics_units_fk character varying NOT NULL,
    c_application_characteristics_sources_fk character varying,
    c_application_characteristics_quality integer NOT NULL,
    c_application_characteristics_comment character varying,
    c_application_characteristics_last_modification date NOT NULL,
    c_application_characteristics_editor character varying NOT NULL
);
 2   DROP TABLE public.tb_application_characteristics;
       public         sozio_e2s_admin_role    false            �           0    0 $   TABLE tb_application_characteristics    COMMENT     l   COMMENT ON TABLE public.tb_application_characteristics IS 'development of the application characteristics';
            public       sozio_e2s_admin_role    false    204            �           0    0 6   COLUMN tb_application_characteristics.c_technology_pfk    COMMENT     h   COMMENT ON COLUMN public.tb_application_characteristics.c_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    204            �           0    0 B   COLUMN tb_application_characteristics.c_investment_options_size_pk    COMMENT     �   COMMENT ON COLUMN public.tb_application_characteristics.c_investment_options_size_pk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       sozio_e2s_admin_role    false    204            �           0    0 T   COLUMN tb_application_characteristics.c_application_characteristics_validity_time_pk    COMMENT     |   COMMENT ON COLUMN public.tb_application_characteristics.c_application_characteristics_validity_time_pk IS '!!! date range';
            public       sozio_e2s_admin_role    false    204            �           0    0 7   COLUMN tb_application_characteristics.c_application_pfk    COMMENT     a   COMMENT ON COLUMN public.tb_application_characteristics.c_application_pfk IS 'app_1, app_2, ..';
            public       sozio_e2s_admin_role    false    204            �           0    0 N   COLUMN tb_application_characteristics.c_application_characteristics_regions_fk    COMMENT     �   COMMENT ON COLUMN public.tb_application_characteristics.c_application_characteristics_regions_fk IS 'refers to NUTS nomenclature (e.g. germany = DE, Baden-Würtemberg = DE1)';
            public       sozio_e2s_admin_role    false    204            �           0    0 N   COLUMN tb_application_characteristics.c_application_characteristics_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_application_characteristics.c_application_characteristics_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    204            �           0    0 $   TABLE tb_application_characteristics    ACL     T   GRANT SELECT ON TABLE public.tb_application_characteristics TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    204            �            1259    239445 $   tb_application_characteristics_types    TABLE     g  CREATE TABLE public.tb_application_characteristics_types (
    c_application_characteristic_types_pk character varying NOT NULL,
    tb_application_characteristic_types_description character varying NOT NULL,
    tb_application_characteristic_types_last_modification date NOT NULL,
    tb_application_characteristic_types_editor character varying NOT NULL
);
 8   DROP TABLE public.tb_application_characteristics_types;
       public         sozio_e2s_admin_role    false            �           0    0 *   TABLE tb_application_characteristics_types    COMMENT     �   COMMENT ON TABLE public.tb_application_characteristics_types IS 'list of assumptions for specific applications (e.g. fullloadhours; share of self suppy)';
            public       sozio_e2s_admin_role    false    205            �           0    0 *   TABLE tb_application_characteristics_types    ACL     Z   GRANT SELECT ON TABLE public.tb_application_characteristics_types TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    205            �            1259    239451    tb_attribute_level    TABLE     �  CREATE TABLE public.tb_attribute_level (
    c_attribute_level_attribute_pfk character varying NOT NULL,
    c_attribute_level_technology_pfk character varying NOT NULL,
    c_attribute_level_investment_options_size_pfk int4range NOT NULL,
    c_attribute_level_investment_options_units_pfk character varying NOT NULL,
    c_attribute_level_pk character varying NOT NULL,
    c_attribute_level_unit_fk character varying,
    c_attribute_level_description character varying NOT NULL,
    c_attribute_level_comment character varying,
    c_attribute_level_quality character varying NOT NULL,
    c_attribute_level_sources_fk character varying NOT NULL,
    c_attribute_level_last_modification date NOT NULL,
    c_attribute_level_editor character varying NOT NULL
);
 &   DROP TABLE public.tb_attribute_level;
       public         sozio_e2s_admin_role    false            �           0    0 :   COLUMN tb_attribute_level.c_attribute_level_technology_pfk    COMMENT     l   COMMENT ON COLUMN public.tb_attribute_level.c_attribute_level_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    206            �           0    0 G   COLUMN tb_attribute_level.c_attribute_level_investment_options_size_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_attribute_level.c_attribute_level_investment_options_size_pfk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       sozio_e2s_admin_role    false    206            �           0    0 6   COLUMN tb_attribute_level.c_attribute_level_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_attribute_level.c_attribute_level_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    206            �           0    0    TABLE tb_attribute_level    ACL     H   GRANT SELECT ON TABLE public.tb_attribute_level TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    206            �            1259    239457    tb_attribute_scenarios    TABLE     �  CREATE TABLE public.tb_attribute_scenarios (
    c_attribute_development_scenario_pk character varying NOT NULL,
    c_attribute_development_attributes_pfk character varying NOT NULL,
    c_attribute_scenarios_technology_pfk character varying NOT NULL,
    c_attribute_development_investment_option_size_pfk int4range NOT NULL,
    c_attribute_development_investment_options_units_pfk character varying NOT NULL,
    c_attribute_scenario_sub_technology_pfk character varying NOT NULL,
    c_attribute_scenario_year_pk integer NOT NULL,
    c_attribute_development_value character varying NOT NULL,
    c_attribute_development_units_fk character varying,
    c_attribute_development_comment character varying,
    c_attribute_development_quality integer NOT NULL,
    c_attribute_development_sources_fk character varying,
    c_attribute_development_last_modification date NOT NULL,
    c_attribute_development_editor character varying NOT NULL
);
 *   DROP TABLE public.tb_attribute_scenarios;
       public         sozio_e2s_admin_role    false            �           0    0    TABLE tb_attribute_scenarios    COMMENT     Y   COMMENT ON TABLE public.tb_attribute_scenarios IS 'contains the attribute developments';
            public       sozio_e2s_admin_role    false    207            �           0    0 A   COLUMN tb_attribute_scenarios.c_attribute_development_scenario_pk    COMMENT     h   COMMENT ON COLUMN public.tb_attribute_scenarios.c_attribute_development_scenario_pk IS 'scenario name';
            public       sozio_e2s_admin_role    false    207            �           0    0 B   COLUMN tb_attribute_scenarios.c_attribute_scenarios_technology_pfk    COMMENT     t   COMMENT ON COLUMN public.tb_attribute_scenarios.c_attribute_scenarios_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    207            �           0    0 P   COLUMN tb_attribute_scenarios.c_attribute_development_investment_option_size_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_attribute_scenarios.c_attribute_development_investment_option_size_pfk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       sozio_e2s_admin_role    false    207            �           0    0 E   COLUMN tb_attribute_scenarios.c_attribute_scenario_sub_technology_pfk    COMMENT     w   COMMENT ON COLUMN public.tb_attribute_scenarios.c_attribute_scenario_sub_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    207            �           0    0 @   COLUMN tb_attribute_scenarios.c_attribute_development_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_attribute_scenarios.c_attribute_development_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    207            �           0    0    TABLE tb_attribute_scenarios    ACL     L   GRANT SELECT ON TABLE public.tb_attribute_scenarios TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    207            �            1259    239463    tb_attributes    TABLE     R  CREATE TABLE public.tb_attributes (
    c_attributes_pk character varying NOT NULL,
    c_attributes_description character varying NOT NULL,
    c_attributes_comment character varying,
    c_attributes_last_modification date NOT NULL,
    c_attributes_editor character varying NOT NULL,
    c_attribute_type character varying NOT NULL
);
 !   DROP TABLE public.tb_attributes;
       public         sozio_e2s_admin_role    false            �           0    0    TABLE tb_attributes    COMMENT     I   COMMENT ON TABLE public.tb_attributes IS 'table contains all utilities';
            public       sozio_e2s_admin_role    false    208            �           0    0    TABLE tb_attributes    ACL     C   GRANT SELECT ON TABLE public.tb_attributes TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    208            �            1259    239474    tb_car_class_shares    TABLE     �  CREATE TABLE public.tb_car_class_shares (
    c_car_class_shares_technology_pfk character varying NOT NULL,
    c_car_class_shares_investment_options_size_pk int4range NOT NULL,
    c_car_class_shares_investment_options_units_pfk character varying NOT NULL,
    c_car_class_shares_validity_year integer NOT NULL,
    c_car_class_shares_stock_share numeric NOT NULL,
    c_car_class_shares_units_fk character varying NOT NULL,
    c_car_class_shares_sources_fk character varying NOT NULL,
    c_car_class_shares_qualiy integer NOT NULL,
    c_car_class_shares_comment character varying,
    c_car_class_shares_last_modified date NOT NULL,
    c_car_class_shares_editor character varying NOT NULL
);
 '   DROP TABLE public.tb_car_class_shares;
       public         postgres    false            �           0    0    TABLE tb_car_class_shares    COMMENT     h   COMMENT ON TABLE public.tb_car_class_shares IS 'shares of car classes according to investment options';
            public       postgres    false    209            �           0    0 <   COLUMN tb_car_class_shares.c_car_class_shares_technology_pfk    COMMENT     n   COMMENT ON COLUMN public.tb_car_class_shares.c_car_class_shares_technology_pfk IS 'abbr. of technology name';
            public       postgres    false    209            �           0    0 H   COLUMN tb_car_class_shares.c_car_class_shares_investment_options_size_pk    COMMENT     �   COMMENT ON COLUMN public.tb_car_class_shares.c_car_class_shares_investment_options_size_pk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       postgres    false    209            �           0    0 8   COLUMN tb_car_class_shares.c_car_class_shares_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_car_class_shares.c_car_class_shares_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       postgres    false    209            �           0    0    TABLE tb_car_class_shares    ACL     G   GRANT ALL ON TABLE public.tb_car_class_shares TO sozio_e2s_admin_role;
            public       postgres    false    209            �            1259    239480    tb_car_stock_scenario    TABLE     T  CREATE TABLE public.tb_car_stock_scenario (
    c_stock_scenario_validity_time_pk int4range NOT NULL,
    c_stock_scenario_scenario_pk character varying NOT NULL,
    c_stock_scenario_technology_pfk character varying NOT NULL,
    c_stock_scenario_annual_growth_rate numeric NOT NULL,
    c_stock_scenario_unit_fk character varying NOT NULL,
    c_stock_scenario_quality integer NOT NULL,
    c_stock_scenario_comment character varying,
    c_stock_scenario_sources_fk character varying,
    c_stock_scenario_last_modified date NOT NULL,
    c_stock_scenario_editor character varying NOT NULL
);
 )   DROP TABLE public.tb_car_stock_scenario;
       public         postgres    false            �           0    0 >   COLUMN tb_car_stock_scenario.c_stock_scenario_validity_time_pk    COMMENT     k   COMMENT ON COLUMN public.tb_car_stock_scenario.c_stock_scenario_validity_time_pk IS 'this is intforrange';
            public       postgres    false    210            �           0    0 <   COLUMN tb_car_stock_scenario.c_stock_scenario_technology_pfk    COMMENT     n   COMMENT ON COLUMN public.tb_car_stock_scenario.c_stock_scenario_technology_pfk IS 'abbr. of technology name';
            public       postgres    false    210            �           0    0 8   COLUMN tb_car_stock_scenario.c_stock_scenario_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_car_stock_scenario.c_stock_scenario_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       postgres    false    210            �           0    0    TABLE tb_car_stock_scenario    ACL     I   GRANT ALL ON TABLE public.tb_car_stock_scenario TO sozio_e2s_admin_role;
            public       postgres    false    210            �            1259    239486    tb_car_target_system    TABLE     .  CREATE TABLE public.tb_car_target_system (
    c_car_target_system_sub_technology_pfk character varying NOT NULL,
    c_car_target_year_pk numeric NOT NULL,
    c_car_target_scenario_pk character varying NOT NULL,
    c_car_target_value character varying NOT NULL,
    c_car_target_value_units_fk character varying NOT NULL,
    c_car_target_sources_fk character varying,
    c_car_target_comment character varying,
    c_car_target_qualiy integer NOT NULL,
    c_car_target_last_modified date NOT NULL,
    c_car_target_editor character varying NOT NULL
);
 (   DROP TABLE public.tb_car_target_system;
       public         postgres    false            �           0    0    TABLE tb_car_target_system    COMMENT     ]   COMMENT ON TABLE public.tb_car_target_system IS 'target system of future technology stock ';
            public       postgres    false    211            �           0    0 B   COLUMN tb_car_target_system.c_car_target_system_sub_technology_pfk    COMMENT     t   COMMENT ON COLUMN public.tb_car_target_system.c_car_target_system_sub_technology_pfk IS 'abbr. of technology name';
            public       postgres    false    211                        0    0 3   COLUMN tb_car_target_system.c_car_target_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_car_target_system.c_car_target_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       postgres    false    211                       0    0    TABLE tb_car_target_system    ACL     H   GRANT ALL ON TABLE public.tb_car_target_system TO sozio_e2s_admin_role;
            public       postgres    false    211            �            1259    239494    tb_cars_stock    TABLE     �  CREATE TABLE public.tb_cars_stock (
    c_technology_pk character varying NOT NULL,
    c_registration_year integer NOT NULL,
    c_stock_year integer NOT NULL,
    c_number_of_cars integer NOT NULL,
    c_sources_pk character varying NOT NULL,
    c_stock_quality integer NOT NULL,
    c_technologies_last_modified date NOT NULL,
    c_technologies_editor character varying NOT NULL
);
 !   DROP TABLE public.tb_cars_stock;
       public         sozio_e2s_admin_user    false                       0    0 !   COLUMN tb_cars_stock.c_sources_pk    COMMENT     s   COMMENT ON COLUMN public.tb_cars_stock.c_sources_pk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_user    false    212            �            1259    239503    tb_consumer_prices    TABLE     �  CREATE TABLE public.tb_consumer_prices (
    c_consumertype_pfk character varying NOT NULL,
    c_consumption_good_pfk character varying NOT NULL,
    c_consumption_prices_scenario character varying NOT NULL,
    c_consumption_prices_validity_time daterange NOT NULL,
    c_consumer_prices_value numeric NOT NULL,
    c_consumer_prices_units_fk character varying NOT NULL,
    c_consumer_prices_fuels_fk character varying,
    c_consumer_prices_sources_fk character varying,
    c_consumer_prices_quality character varying NOT NULL,
    c_consumer_prices_comment character varying,
    c_consumer_prices_last_modification date NOT NULL,
    c_consumer_prices_editor character varying NOT NULL
);
 &   DROP TABLE public.tb_consumer_prices;
       public         sozio_e2s_admin_role    false                       0    0 <   COLUMN tb_consumer_prices.c_consumption_prices_validity_time    COMMENT     d   COMMENT ON COLUMN public.tb_consumer_prices.c_consumption_prices_validity_time IS '!!! date range';
            public       sozio_e2s_admin_role    false    213                       0    0 4   COLUMN tb_consumer_prices.c_consumer_prices_fuels_fk    COMMENT     h   COMMENT ON COLUMN public.tb_consumer_prices.c_consumer_prices_fuels_fk IS 'table containing all fuels';
            public       sozio_e2s_admin_role    false    213                       0    0 6   COLUMN tb_consumer_prices.c_consumer_prices_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_consumer_prices.c_consumer_prices_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    213                       0    0    TABLE tb_consumer_prices    ACL     H   GRANT SELECT ON TABLE public.tb_consumer_prices TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    213            �            1259    239509    tb_consumertype    TABLE       CREATE TABLE public.tb_consumertype (
    c_consumertype_pk character varying NOT NULL,
    c_consumertype_description character varying NOT NULL,
    c_consumer_type_last_modification date NOT NULL,
    c_consumer_types_editor character varying NOT NULL
);
 #   DROP TABLE public.tb_consumertype;
       public         sozio_e2s_admin_role    false                       0    0 8   COLUMN tb_consumertype.c_consumer_type_last_modification    COMMENT     k   COMMENT ON COLUMN public.tb_consumertype.c_consumer_type_last_modification IS 'date of last modification';
            public       sozio_e2s_admin_role    false    214                       0    0    TABLE tb_consumertype    ACL     E   GRANT SELECT ON TABLE public.tb_consumertype TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    214            �            1259    239519    tb_consumption_good    TABLE       CREATE TABLE public.tb_consumption_good (
    c_consumption_good_pk character varying NOT NULL,
    c_consumption_good_description character varying NOT NULL,
    c_consumption_good_last_modification date NOT NULL,
    c_consumption_good_editor character varying NOT NULL
);
 '   DROP TABLE public.tb_consumption_good;
       public         sozio_e2s_admin_role    false            	           0    0 ?   COLUMN tb_consumption_good.c_consumption_good_last_modification    COMMENT     r   COMMENT ON COLUMN public.tb_consumption_good.c_consumption_good_last_modification IS 'date of last modification';
            public       sozio_e2s_admin_role    false    215            
           0    0    TABLE tb_consumption_good    ACL     I   GRANT SELECT ON TABLE public.tb_consumption_good TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    215            �            1259    239525    tb_economic_basic_parameter    TABLE     �  CREATE TABLE public.tb_economic_basic_parameter (
    c_economic_basic_parameter_type_pk character varying NOT NULL,
    c_economic_basic_parameter_validity_time daterange NOT NULL,
    c_economic_basic_parameter_scenario character varying NOT NULL,
    c_economic_basic_parameter_value numeric NOT NULL,
    c_economic_basic_parameter_unit_fk character varying NOT NULL,
    c_economic_basic_parameter_source_fk character varying NOT NULL,
    c_economic_basic_parameter_comment character varying,
    c_economic_basic_parameter_quality character varying NOT NULL,
    c_economic_basic_parameter_last_modificcation date NOT NULL,
    c_economic_basic_parameter_editor character varying NOT NULL
);
 /   DROP TABLE public.tb_economic_basic_parameter;
       public         sozio_e2s_admin_role    false                       0    0 !   TABLE tb_economic_basic_parameter    COMMENT     �   COMMENT ON TABLE public.tb_economic_basic_parameter IS 'economic parameter like inflation which are not dependend on technologies';
            public       sozio_e2s_admin_role    false    216                       0    0 E   COLUMN tb_economic_basic_parameter.c_economic_basic_parameter_type_pk    COMMENT     �   COMMENT ON COLUMN public.tb_economic_basic_parameter.c_economic_basic_parameter_type_pk IS 'type of economic parameter (e.g. Inflation)';
            public       sozio_e2s_admin_role    false    216                       0    0 K   COLUMN tb_economic_basic_parameter.c_economic_basic_parameter_validity_time    COMMENT     �   COMMENT ON COLUMN public.tb_economic_basic_parameter.c_economic_basic_parameter_validity_time IS 'Date range of validity 
!!!put date range as type!!!';
            public       sozio_e2s_admin_role    false    216                       0    0 F   COLUMN tb_economic_basic_parameter.c_economic_basic_parameter_scenario    COMMENT     �   COMMENT ON COLUMN public.tb_economic_basic_parameter.c_economic_basic_parameter_scenario IS 'Scenario of basic parameter development';
            public       sozio_e2s_admin_role    false    216                       0    0 C   COLUMN tb_economic_basic_parameter.c_economic_basic_parameter_value    COMMENT     �   COMMENT ON COLUMN public.tb_economic_basic_parameter.c_economic_basic_parameter_value IS 'numeric value of economic parameter';
            public       sozio_e2s_admin_role    false    216                       0    0 G   COLUMN tb_economic_basic_parameter.c_economic_basic_parameter_source_fk    COMMENT     �   COMMENT ON COLUMN public.tb_economic_basic_parameter.c_economic_basic_parameter_source_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    216                       0    0 E   COLUMN tb_economic_basic_parameter.c_economic_basic_parameter_comment    COMMENT     m   COMMENT ON COLUMN public.tb_economic_basic_parameter.c_economic_basic_parameter_comment IS 'Comment to row';
            public       sozio_e2s_admin_role    false    216                       0    0 E   COLUMN tb_economic_basic_parameter.c_economic_basic_parameter_quality    COMMENT     �   COMMENT ON COLUMN public.tb_economic_basic_parameter.c_economic_basic_parameter_quality IS 'Quality of value (1=refernced, 2= reasoned assumption; 3=assumption)';
            public       sozio_e2s_admin_role    false    216                       0    0 P   COLUMN tb_economic_basic_parameter.c_economic_basic_parameter_last_modificcation    COMMENT     �   COMMENT ON COLUMN public.tb_economic_basic_parameter.c_economic_basic_parameter_last_modificcation IS 'date of last modification';
            public       sozio_e2s_admin_role    false    216                       0    0 D   COLUMN tb_economic_basic_parameter.c_economic_basic_parameter_editor    COMMENT     r   COMMENT ON COLUMN public.tb_economic_basic_parameter.c_economic_basic_parameter_editor IS 'editor of data entry';
            public       sozio_e2s_admin_role    false    216                       0    0 !   TABLE tb_economic_basic_parameter    ACL     Q   GRANT SELECT ON TABLE public.tb_economic_basic_parameter TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    216            �            1259    239531    tb_economic_basics_types    TABLE     c  CREATE TABLE public.tb_economic_basics_types (
    c_economic_basics_types_pk character varying NOT NULL,
    c_economic_basics_types_description character varying NOT NULL,
    c_economic_basics_types_comment character varying,
    c_economic_basics_types_last_modification date NOT NULL,
    c_economic_basics_types_editor character varying NOT NULL
);
 ,   DROP TABLE public.tb_economic_basics_types;
       public         sozio_e2s_admin_role    false                       0    0    TABLE tb_economic_basics_types    COMMENT     _   COMMENT ON TABLE public.tb_economic_basics_types IS 'types of basic economic parameter types';
            public       sozio_e2s_admin_role    false    217                       0    0 :   COLUMN tb_economic_basics_types.c_economic_basics_types_pk    COMMENT     v   COMMENT ON COLUMN public.tb_economic_basics_types.c_economic_basics_types_pk IS 'primary key of economic basis type';
            public       sozio_e2s_admin_role    false    217                       0    0 C   COLUMN tb_economic_basics_types.c_economic_basics_types_description    COMMENT     �   COMMENT ON COLUMN public.tb_economic_basics_types.c_economic_basics_types_description IS 'long name of economic parameter type';
            public       sozio_e2s_admin_role    false    217                       0    0 ?   COLUMN tb_economic_basics_types.c_economic_basics_types_comment    COMMENT     o   COMMENT ON COLUMN public.tb_economic_basics_types.c_economic_basics_types_comment IS 'comment on description';
            public       sozio_e2s_admin_role    false    217                       0    0 I   COLUMN tb_economic_basics_types.c_economic_basics_types_last_modification    COMMENT     |   COMMENT ON COLUMN public.tb_economic_basics_types.c_economic_basics_types_last_modification IS 'date of last modification';
            public       sozio_e2s_admin_role    false    217                       0    0 >   COLUMN tb_economic_basics_types.c_economic_basics_types_editor    COMMENT     l   COMMENT ON COLUMN public.tb_economic_basics_types.c_economic_basics_types_editor IS 'editor of data entry';
            public       sozio_e2s_admin_role    false    217                       0    0    TABLE tb_economic_basics_types    ACL     N   GRANT SELECT ON TABLE public.tb_economic_basics_types TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    217            �            1259    239537    tb_economic_parameter    TABLE     H  CREATE TABLE public.tb_economic_parameter (
    c_technology_pfk character varying NOT NULL,
    c_investment_options_size_pk int4range NOT NULL,
    c_investment_options_units_pfk character varying NOT NULL,
    c_regions_pfk character varying NOT NULL,
    c_economic_parameter_validity_time daterange NOT NULL,
    c_economic_parameter_types_pfk character varying NOT NULL,
    c_economic_parameter_value numeric NOT NULL,
    c_economic_parameter_unit_fk character varying NOT NULL,
    c_economic_parameter_scenario_pk character varying NOT NULL,
    c_economic_parameter_sources_fk character varying,
    c_economic_parameter_comment character varying,
    c_economic_parameter_quality character varying NOT NULL,
    c_economic_parameter_last_modification date NOT NULL,
    c_economic_parameter_editor character varying NOT NULL
);
 )   DROP TABLE public.tb_economic_parameter;
       public         sozio_e2s_admin_role    false                       0    0    TABLE tb_economic_parameter    COMMENT     v   COMMENT ON TABLE public.tb_economic_parameter IS 'table contains all economic parameter (political, cost_parameter)';
            public       sozio_e2s_admin_role    false    218                       0    0 -   COLUMN tb_economic_parameter.c_technology_pfk    COMMENT     _   COMMENT ON COLUMN public.tb_economic_parameter.c_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    218                       0    0 9   COLUMN tb_economic_parameter.c_investment_options_size_pk    COMMENT     �   COMMENT ON COLUMN public.tb_economic_parameter.c_investment_options_size_pk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       sozio_e2s_admin_role    false    218                        0    0 ?   COLUMN tb_economic_parameter.c_economic_parameter_validity_time    COMMENT     y   COMMENT ON COLUMN public.tb_economic_parameter.c_economic_parameter_validity_time IS 'date range;
!!! Update data type';
            public       sozio_e2s_admin_role    false    218            !           0    0 <   COLUMN tb_economic_parameter.c_economic_parameter_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_economic_parameter.c_economic_parameter_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    218            "           0    0    TABLE tb_economic_parameter    ACL     K   GRANT SELECT ON TABLE public.tb_economic_parameter TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    218            �            1259    239545    tb_economic_parameter_type    TABLE     e  CREATE TABLE public.tb_economic_parameter_type (
    c_economic_parameter_types_pk character varying NOT NULL,
    c_economic_parameter_description character varying NOT NULL,
    c_economic_parameter_comment character varying NOT NULL,
    c_economic_parameter_last_modification date NOT NULL,
    c_economic_parameter_editor character varying NOT NULL
);
 .   DROP TABLE public.tb_economic_parameter_type;
       public         sozio_e2s_admin_role    false            #           0    0     TABLE tb_economic_parameter_type    COMMENT     �   COMMENT ON TABLE public.tb_economic_parameter_type IS 'table contains all economic parameter types (CAPEX, OPEX etc.) with a description';
            public       sozio_e2s_admin_role    false    219            $           0    0 ?   COLUMN tb_economic_parameter_type.c_economic_parameter_types_pk    COMMENT     v   COMMENT ON COLUMN public.tb_economic_parameter_type.c_economic_parameter_types_pk IS 'ID of economic parameter type';
            public       sozio_e2s_admin_role    false    219            %           0    0 B   COLUMN tb_economic_parameter_type.c_economic_parameter_description    COMMENT     �   COMMENT ON COLUMN public.tb_economic_parameter_type.c_economic_parameter_description IS 'long name of economic parameter type';
            public       sozio_e2s_admin_role    false    219            &           0    0 >   COLUMN tb_economic_parameter_type.c_economic_parameter_comment    COMMENT     u   COMMENT ON COLUMN public.tb_economic_parameter_type.c_economic_parameter_comment IS 'long description of parameter';
            public       sozio_e2s_admin_role    false    219            '           0    0 H   COLUMN tb_economic_parameter_type.c_economic_parameter_last_modification    COMMENT     {   COMMENT ON COLUMN public.tb_economic_parameter_type.c_economic_parameter_last_modification IS 'date of last modification';
            public       sozio_e2s_admin_role    false    219            (           0    0 =   COLUMN tb_economic_parameter_type.c_economic_parameter_editor    COMMENT     k   COMMENT ON COLUMN public.tb_economic_parameter_type.c_economic_parameter_editor IS 'editor of data entry';
            public       sozio_e2s_admin_role    false    219            )           0    0     TABLE tb_economic_parameter_type    ACL     P   GRANT SELECT ON TABLE public.tb_economic_parameter_type TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    219            �            1259    239551    tb_financial_parameter    TABLE     �  CREATE TABLE public.tb_financial_parameter (
    c_investors_pfk character varying NOT NULL,
    c_technology_pfk character varying NOT NULL,
    c_investment_options_size_pk int4range NOT NULL,
    c_investment_options_units_pfk character varying NOT NULL,
    c_financial_parameter_scenario_pk character varying NOT NULL,
    c_financial_parameter_types_pk character varying NOT NULL,
    c_financial_parameter_value numeric NOT NULL,
    c_financial_parameter_validity_time_pk daterange NOT NULL,
    c_financial_parameter_regions_fk character varying NOT NULL,
    c_financial_parameter_units_fk character varying NOT NULL,
    c_financial_parameter_sources_fk character varying,
    c_financial_parameter_comment character varying,
    c_financial_parameter_quality character varying NOT NULL,
    c_financial_parameter_last_modification date NOT NULL,
    c_financial_parameter_editor character varying NOT NULL
);
 *   DROP TABLE public.tb_financial_parameter;
       public         sozio_e2s_admin_role    false            *           0    0 -   COLUMN tb_financial_parameter.c_investors_pfk    COMMENT     s   COMMENT ON COLUMN public.tb_financial_parameter.c_investors_pfk IS 'investor key (private = priv, evu = EVU,...)';
            public       sozio_e2s_admin_role    false    220            +           0    0 .   COLUMN tb_financial_parameter.c_technology_pfk    COMMENT     `   COMMENT ON COLUMN public.tb_financial_parameter.c_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    220            ,           0    0 :   COLUMN tb_financial_parameter.c_investment_options_size_pk    COMMENT     �   COMMENT ON COLUMN public.tb_financial_parameter.c_investment_options_size_pk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       sozio_e2s_admin_role    false    220            -           0    0 D   COLUMN tb_financial_parameter.c_financial_parameter_validity_time_pk    COMMENT     l   COMMENT ON COLUMN public.tb_financial_parameter.c_financial_parameter_validity_time_pk IS '!!! Date range';
            public       sozio_e2s_admin_role    false    220            .           0    0 >   COLUMN tb_financial_parameter.c_financial_parameter_regions_fk    COMMENT     �   COMMENT ON COLUMN public.tb_financial_parameter.c_financial_parameter_regions_fk IS 'refers to NUTS nomenclature (e.g. germany = DE, Baden-Würtemberg = DE1)';
            public       sozio_e2s_admin_role    false    220            /           0    0 >   COLUMN tb_financial_parameter.c_financial_parameter_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_financial_parameter.c_financial_parameter_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    220            0           0    0 E   COLUMN tb_financial_parameter.c_financial_parameter_last_modification    COMMENT     x   COMMENT ON COLUMN public.tb_financial_parameter.c_financial_parameter_last_modification IS 'date of last modification';
            public       sozio_e2s_admin_role    false    220            1           0    0    TABLE tb_financial_parameter    ACL     L   GRANT SELECT ON TABLE public.tb_financial_parameter TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    220            �            1259    239557    tb_financial_parameter_types    TABLE     {  CREATE TABLE public.tb_financial_parameter_types (
    c_financial_parameter_types_pk character varying NOT NULL,
    c_financial_parameter_types_description character varying NOT NULL,
    c_financial_parameter_types_comment character varying,
    c_financial_parameter_types_last_modification date NOT NULL,
    c_financial_parameter_types_editor character varying NOT NULL
);
 0   DROP TABLE public.tb_financial_parameter_types;
       public         sozio_e2s_admin_role    false            2           0    0 "   TABLE tb_financial_parameter_types    ACL     R   GRANT SELECT ON TABLE public.tb_financial_parameter_types TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    221            �            1259    239563    tb_fuels    TABLE     4  CREATE TABLE public.tb_fuels (
    c_fuels_pk character varying(100) NOT NULL,
    c_fuels_description character varying(50) NOT NULL,
    c_fuels_comment character varying(150),
    c_fuels_last_modified date DEFAULT ('now'::text)::date NOT NULL,
    c_technologies_editor character varying(50) NOT NULL
);
    DROP TABLE public.tb_fuels;
       public         sozio_e2s_admin_role    false            3           0    0    TABLE tb_fuels    ACL     >   GRANT SELECT ON TABLE public.tb_fuels TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    222            �            1259    239567    tb_grid_level    TABLE     �  CREATE TABLE public.tb_grid_level (
    c_grid_level_pk character varying NOT NULL,
    c_voltage_level character varying NOT NULL,
    c_voltage_level_units_fk character varying NOT NULL,
    c_grid_level_regions_fk character varying NOT NULL,
    c_grid_level_comment character varying,
    c_grid_level_sources_fk character varying,
    c_grid_level_quality integer NOT NULL,
    c_grid_level_last_modification date NOT NULL,
    c_grid_level_last_editor character varying NOT NULL
);
 !   DROP TABLE public.tb_grid_level;
       public         sozio_e2s_admin_role    false            4           0    0    TABLE tb_grid_level    COMMENT     <   COMMENT ON TABLE public.tb_grid_level IS 'all grid levels';
            public       sozio_e2s_admin_role    false    223            5           0    0 ,   COLUMN tb_grid_level.c_grid_level_regions_fk    COMMENT     �   COMMENT ON COLUMN public.tb_grid_level.c_grid_level_regions_fk IS 'refers to NUTS nomenclature (e.g. germany = DE, Baden-Würtemberg = DE1)';
            public       sozio_e2s_admin_role    false    223            6           0    0 ,   COLUMN tb_grid_level.c_grid_level_sources_fk    COMMENT     ~   COMMENT ON COLUMN public.tb_grid_level.c_grid_level_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    223            7           0    0    TABLE tb_grid_level    ACL     C   GRANT SELECT ON TABLE public.tb_grid_level TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    223            �            1259    239573    tb_importances    TABLE     �  CREATE TABLE public.tb_importances (
    c_importance_attribute_pfk character varying NOT NULL,
    c_importances_technology_pfk character varying NOT NULL,
    c_importances_investment_options_size_pfk int4range NOT NULL,
    c_importances_investment_options_units_pfk character varying NOT NULL,
    c_importance_respondend_pfk character varying NOT NULL,
    c_importance_level character varying NOT NULL,
    c_importance_value numeric NOT NULL,
    c_importance_comment character varying NOT NULL,
    c_importance_quality character varying NOT NULL,
    c_importance_sources_fk character varying,
    c_importance_last_modification date NOT NULL,
    c_importance_editor character varying NOT NULL
);
 "   DROP TABLE public.tb_importances;
       public         sozio_e2s_admin_role    false            8           0    0 2   COLUMN tb_importances.c_importances_technology_pfk    COMMENT     d   COMMENT ON COLUMN public.tb_importances.c_importances_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    224            9           0    0 ?   COLUMN tb_importances.c_importances_investment_options_size_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_importances.c_importances_investment_options_size_pfk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       sozio_e2s_admin_role    false    224            :           0    0 -   COLUMN tb_importances.c_importance_sources_fk    COMMENT        COMMENT ON COLUMN public.tb_importances.c_importance_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    224            ;           0    0    TABLE tb_importances    ACL     D   GRANT SELECT ON TABLE public.tb_importances TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    224            �            1259    239579    tb_investment_options    TABLE     5  CREATE TABLE public.tb_investment_options (
    c_technology_pfk character varying NOT NULL,
    c_investment_options_size_pk int4range NOT NULL,
    c_investment_options_units_pfk character varying NOT NULL,
    c_investment_options_description character varying NOT NULL,
    c_investment_options_sources_fk character varying,
    c_investment_options_quality integer NOT NULL,
    c_investment_options_comment character varying,
    c_investment_options_last_modification character varying NOT NULL,
    c_investment_options_editor character varying NOT NULL
);
 )   DROP TABLE public.tb_investment_options;
       public         sozio_e2s_admin_role    false            <           0    0    TABLE tb_investment_options    COMMENT     �   COMMENT ON TABLE public.tb_investment_options IS 'Table defines all investment options according to their size. e.g. 
Electric car small PV rooftop etc.';
            public       sozio_e2s_admin_role    false    225            =           0    0 -   COLUMN tb_investment_options.c_technology_pfk    COMMENT     _   COMMENT ON COLUMN public.tb_investment_options.c_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    225            >           0    0 9   COLUMN tb_investment_options.c_investment_options_size_pk    COMMENT     �   COMMENT ON COLUMN public.tb_investment_options.c_investment_options_size_pk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...!!!Datatype: Integer range';
            public       sozio_e2s_admin_role    false    225            ?           0    0 =   COLUMN tb_investment_options.c_investment_options_description    COMMENT     y   COMMENT ON COLUMN public.tb_investment_options.c_investment_options_description IS 'description of investment decision';
            public       sozio_e2s_admin_role    false    225            @           0    0 <   COLUMN tb_investment_options.c_investment_options_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_investment_options.c_investment_options_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    225            A           0    0 9   COLUMN tb_investment_options.c_investment_options_quality    COMMENT     �   COMMENT ON COLUMN public.tb_investment_options.c_investment_options_quality IS '1 -> related to citable source; 2 -> very good guessed assumption; 3 -> assumption';
            public       sozio_e2s_admin_role    false    225            B           0    0 9   COLUMN tb_investment_options.c_investment_options_comment    COMMENT     �   COMMENT ON COLUMN public.tb_investment_options.c_investment_options_comment IS 'comment on source (e.g. assumption is that,...)';
            public       sozio_e2s_admin_role    false    225            C           0    0 C   COLUMN tb_investment_options.c_investment_options_last_modification    COMMENT     v   COMMENT ON COLUMN public.tb_investment_options.c_investment_options_last_modification IS 'date of last modification';
            public       sozio_e2s_admin_role    false    225            D           0    0    TABLE tb_investment_options    ACL     K   GRANT SELECT ON TABLE public.tb_investment_options TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    225            �            1259    239585    tb_investor_stock_share    TABLE     �  CREATE TABLE public.tb_investor_stock_share (
    c_investor_stock_share_technology_pk character varying NOT NULL,
    c_investor_stock_share_investors_pk character varying NOT NULL,
    c_investor_stock_share_validity_year_pk integer NOT NULL,
    c_investor_stock_share_stock_share numeric NOT NULL,
    c_investor_stock_shares_units_fk character varying NOT NULL,
    c_investor_stock_shares_sources_fk character varying NOT NULL,
    c_investor_stock_shares_qualiy integer NOT NULL,
    c_investor_stock_shares_comment character varying,
    c_investor_stock_shares_last_modified date NOT NULL,
    c_investor_stock_shares_editor character varying NOT NULL
);
 +   DROP TABLE public.tb_investor_stock_share;
       public         postgres    false            E           0    0    TABLE tb_investor_stock_share    COMMENT     u   COMMENT ON TABLE public.tb_investor_stock_share IS 'contains the shares of investors in relation to the technology';
            public       postgres    false    226            F           0    0 C   COLUMN tb_investor_stock_share.c_investor_stock_share_technology_pk    COMMENT     u   COMMENT ON COLUMN public.tb_investor_stock_share.c_investor_stock_share_technology_pk IS 'abbr. of technology name';
            public       postgres    false    226            G           0    0 ?   COLUMN tb_investor_stock_share.c_investor_stock_shares_units_fk    COMMENT     �   COMMENT ON COLUMN public.tb_investor_stock_share.c_investor_stock_shares_units_fk IS 'primary key refers to bit tex keys using citavi database';
            public       postgres    false    226            H           0    0    TABLE tb_investor_stock_share    ACL     K   GRANT ALL ON TABLE public.tb_investor_stock_share TO sozio_e2s_admin_role;
            public       postgres    false    226            �            1259    239591    tb_investors    TABLE     L  CREATE TABLE public.tb_investors (
    c_investors_pk character varying NOT NULL,
    c_investors_description character varying NOT NULL,
    c_investors_level integer NOT NULL,
    c_investors_comment character varying NOT NULL,
    c_investors_last_modification date NOT NULL,
    c_investors_editor character varying NOT NULL
);
     DROP TABLE public.tb_investors;
       public         sozio_e2s_admin_role    false            I           0    0    TABLE tb_investors    COMMENT     �   COMMENT ON TABLE public.tb_investors IS 'tabel contains an overview on all investors that are used - serves as a parent table';
            public       sozio_e2s_admin_role    false    227            J           0    0 +   COLUMN tb_investors.c_investors_description    COMMENT     s   COMMENT ON COLUMN public.tb_investors.c_investors_description IS 'full name of investor (utility, private, etc.)';
            public       sozio_e2s_admin_role    false    227            K           0    0 '   COLUMN tb_investors.c_investors_comment    COMMENT     p   COMMENT ON COLUMN public.tb_investors.c_investors_comment IS 'comment on source (e.g. assumption is that,...)';
            public       sozio_e2s_admin_role    false    227            L           0    0    TABLE tb_investors    ACL     B   GRANT SELECT ON TABLE public.tb_investors TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    227            �            1259    239597    tb_market_phase    TABLE     �  CREATE TABLE public.tb_market_phase (
    c_market_phase_pk character varying NOT NULL,
    c_market_phase_description character varying NOT NULL,
    c_market_phase_value numeric,
    c_market_phase_units_fk character varying,
    c_market_phase_quality integer NOT NULL,
    c_market_phase_comment character varying,
    c_market_phase_sources_fk character varying,
    c_market_phase_last_modification date NOT NULL,
    c_market_phase_editor character varying NOT NULL
);
 #   DROP TABLE public.tb_market_phase;
       public         sozio_e2s_admin_role    false            M           0    0 (   COLUMN tb_market_phase.c_market_phase_pk    COMMENT     P   COMMENT ON COLUMN public.tb_market_phase.c_market_phase_pk IS 'mp_1, mp2, ...';
            public       sozio_e2s_admin_role    false    228            N           0    0 -   COLUMN tb_market_phase.c_market_phase_quality    COMMENT     �   COMMENT ON COLUMN public.tb_market_phase.c_market_phase_quality IS '1 -> related to citable source; 2 -> very good guessed assumption; 3 -> assumption';
            public       sozio_e2s_admin_role    false    228            O           0    0 -   COLUMN tb_market_phase.c_market_phase_comment    COMMENT     v   COMMENT ON COLUMN public.tb_market_phase.c_market_phase_comment IS 'comment on source (e.g. assumption is that,...)';
            public       sozio_e2s_admin_role    false    228            P           0    0 0   COLUMN tb_market_phase.c_market_phase_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_market_phase.c_market_phase_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    228            Q           0    0    TABLE tb_market_phase    ACL     E   GRANT SELECT ON TABLE public.tb_market_phase TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    228            �            1259    239617    tb_political_incentives    TABLE     �  CREATE TABLE public.tb_political_incentives (
    c_technology_pfk character varying NOT NULL,
    c_investment_options_size_pfk int4range NOT NULL,
    c_investment_options_units_pfk character varying NOT NULL,
    c_political_incentive_validity_time daterange NOT NULL,
    c_political_incentive_region character varying NOT NULL,
    c_political_incentive_application_fk character varying NOT NULL,
    c_political_instrument_type_fk character varying NOT NULL,
    c_political_instrument_scenario character varying NOT NULL,
    c_political_incentive_value numeric NOT NULL,
    c_political_incentive_unit_fk character varying NOT NULL,
    c_political_incentive_sources_fk character varying,
    c_political_incentive_quality integer NOT NULL,
    c_political_incentive_comment character varying,
    c_political_incentive_last_modification date NOT NULL,
    c_political_incentive_editor character varying NOT NULL
);
 +   DROP TABLE public.tb_political_incentives;
       public         sozio_e2s_admin_role    false            R           0    0    TABLE tb_political_incentives    COMMENT     l   COMMENT ON TABLE public.tb_political_incentives IS 'table containing developments of political incentives';
            public       sozio_e2s_admin_role    false    229            S           0    0 /   COLUMN tb_political_incentives.c_technology_pfk    COMMENT     a   COMMENT ON COLUMN public.tb_political_incentives.c_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    229            T           0    0 <   COLUMN tb_political_incentives.c_investment_options_size_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_political_incentives.c_investment_options_size_pfk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       sozio_e2s_admin_role    false    229            U           0    0 B   COLUMN tb_political_incentives.c_political_incentive_validity_time    COMMENT     j   COMMENT ON COLUMN public.tb_political_incentives.c_political_incentive_validity_time IS '!!! date range';
            public       sozio_e2s_admin_role    false    229            V           0    0 ;   COLUMN tb_political_incentives.c_political_incentive_region    COMMENT     �   COMMENT ON COLUMN public.tb_political_incentives.c_political_incentive_region IS 'refers to NUTS nomenclature (e.g. germany = DE, Baden-Würtemberg = DE1)';
            public       sozio_e2s_admin_role    false    229            W           0    0 C   COLUMN tb_political_incentives.c_political_incentive_application_fk    COMMENT     m   COMMENT ON COLUMN public.tb_political_incentives.c_political_incentive_application_fk IS 'app_1, app_2, ..';
            public       sozio_e2s_admin_role    false    229            X           0    0 =   COLUMN tb_political_incentives.c_political_instrument_type_fk    COMMENT     w   COMMENT ON COLUMN public.tb_political_incentives.c_political_instrument_type_fk IS 'abbreviation of instrument as pk';
            public       sozio_e2s_admin_role    false    229            Y           0    0 >   COLUMN tb_political_incentives.c_political_instrument_scenario    COMMENT     v   COMMENT ON COLUMN public.tb_political_incentives.c_political_instrument_scenario IS 'identifies different scenarios';
            public       sozio_e2s_admin_role    false    229            Z           0    0 :   COLUMN tb_political_incentives.c_political_incentive_value    COMMENT     k   COMMENT ON COLUMN public.tb_political_incentives.c_political_incentive_value IS 'value it self (e.g. 7 )';
            public       sozio_e2s_admin_role    false    229            [           0    0 ?   COLUMN tb_political_incentives.c_political_incentive_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_political_incentives.c_political_incentive_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    229            \           0    0    TABLE tb_political_incentives    ACL     M   GRANT SELECT ON TABLE public.tb_political_incentives TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    229            �            1259    239623    tb_political_instrument_types    TABLE     H  CREATE TABLE public.tb_political_instrument_types (
    c_political_instrument_type_pk character varying NOT NULL,
    tb_political_instrument_types_description character varying NOT NULL,
    tb_political_instruments_types_last_modification date NOT NULL,
    tb_political_instrument_types_editor character varying NOT NULL
);
 1   DROP TABLE public.tb_political_instrument_types;
       public         sozio_e2s_admin_role    false            ]           0    0 #   TABLE tb_political_instrument_types    COMMENT     �   COMMENT ON TABLE public.tb_political_instrument_types IS 'definition of the different political instruments (e.g. feed in tarif)';
            public       sozio_e2s_admin_role    false    230            ^           0    0 C   COLUMN tb_political_instrument_types.c_political_instrument_type_pk    COMMENT     }   COMMENT ON COLUMN public.tb_political_instrument_types.c_political_instrument_type_pk IS 'abbreviation of instrument as pk';
            public       sozio_e2s_admin_role    false    230            _           0    0 #   TABLE tb_political_instrument_types    ACL     S   GRANT SELECT ON TABLE public.tb_political_instrument_types TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    230            �            1259    239641    tb_potlitical_target    TABLE     �  CREATE TABLE public.tb_potlitical_target (
    c_regions_pfk character varying NOT NULL,
    c_technology_pfk character varying NOT NULL,
    c_investment_options_size_pk int4range NOT NULL,
    c_investment_options_units_pfk character varying NOT NULL,
    c_political_targetl_value numeric NOT NULL,
    c_political_target_validity_time date NOT NULL,
    c_political_targetl_unit character varying NOT NULL,
    c_political_target_sources_fk character varying NOT NULL,
    c_political_target_quality integer NOT NULL,
    c_political_target_comment character(1) NOT NULL,
    c_political_target_last_modification character varying NOT NULL,
    c_political_target_editor character varying NOT NULL
);
 (   DROP TABLE public.tb_potlitical_target;
       public         sozio_e2s_admin_role    false            `           0    0    TABLE tb_potlitical_target    COMMENT     h   COMMENT ON TABLE public.tb_potlitical_target IS 'tb_potlitical_target related to an investment option';
            public       sozio_e2s_admin_role    false    231            a           0    0 )   COLUMN tb_potlitical_target.c_regions_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_potlitical_target.c_regions_pfk IS 'refers to NUTS nomenclature (e.g. germany = DE, Baden-Würtemberg = DE1)';
            public       sozio_e2s_admin_role    false    231            b           0    0 ,   COLUMN tb_potlitical_target.c_technology_pfk    COMMENT     ^   COMMENT ON COLUMN public.tb_potlitical_target.c_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    231            c           0    0 8   COLUMN tb_potlitical_target.c_investment_options_size_pk    COMMENT     �   COMMENT ON COLUMN public.tb_potlitical_target.c_investment_options_size_pk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       sozio_e2s_admin_role    false    231            d           0    0 <   COLUMN tb_potlitical_target.c_political_target_validity_time    COMMENT     d   COMMENT ON COLUMN public.tb_potlitical_target.c_political_target_validity_time IS '!!! date range';
            public       sozio_e2s_admin_role    false    231            e           0    0 9   COLUMN tb_potlitical_target.c_political_target_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_potlitical_target.c_political_target_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    231            f           0    0 6   COLUMN tb_potlitical_target.c_political_target_quality    COMMENT     �   COMMENT ON COLUMN public.tb_potlitical_target.c_political_target_quality IS '1 -> related to citable source; 2 -> very good guessed assumption; 3 -> assumption';
            public       sozio_e2s_admin_role    false    231            g           0    0 6   COLUMN tb_potlitical_target.c_political_target_comment    COMMENT     �   COMMENT ON COLUMN public.tb_potlitical_target.c_political_target_comment IS 'comment on data entry; how was the assumption made; any nescessary information';
            public       sozio_e2s_admin_role    false    231            h           0    0 5   COLUMN tb_potlitical_target.c_political_target_editor    COMMENT     c   COMMENT ON COLUMN public.tb_potlitical_target.c_political_target_editor IS 'editor of data entry';
            public       sozio_e2s_admin_role    false    231            i           0    0    TABLE tb_potlitical_target    ACL     J   GRANT SELECT ON TABLE public.tb_potlitical_target TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    231            �            1259    239647    tb_power_plant_status    TABLE     M  CREATE TABLE public.tb_power_plant_status (
    c_power_plant_status_pk character varying NOT NULL,
    c_power_plant_status_description character varying NOT NULL,
    c_power_plant_status_comment character varying,
    c_power_plant_status_last_modified date NOT NULL,
    c_power_plant_status_editor character varying NOT NULL
);
 )   DROP TABLE public.tb_power_plant_status;
       public         sozio_e2s_admin_role    false            j           0    0    TABLE tb_power_plant_status    ACL     K   GRANT SELECT ON TABLE public.tb_power_plant_status TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    232            �            1259    239659    tb_profile_characteristics    TABLE     �  CREATE TABLE public.tb_profile_characteristics (
    c_profile_pk character varying NOT NULL,
    c_profile_scenario_pk character varying NOT NULL,
    c_profile_reference_year_pk integer NOT NULL,
    c_profile_characteristrics_type_pfk character varying NOT NULL,
    c_profile_comment character varying,
    c_profile_quality character varying NOT NULL,
    c_profile_sources_fk character varying,
    c_profile_last_modified date NOT NULL,
    c_profile_editor character varying NOT NULL
);
 .   DROP TABLE public.tb_profile_characteristics;
       public         postgres    false            k           0    0     TABLE tb_profile_characteristics    COMMENT     �   COMMENT ON TABLE public.tb_profile_characteristics IS 'Characterisation of the profiles (region, scenario, reference year, technology, profile_type) ';
            public       postgres    false    233            l           0    0 .   COLUMN tb_profile_characteristics.c_profile_pk    COMMENT     h   COMMENT ON COLUMN public.tb_profile_characteristics.c_profile_pk IS 'unique identifier of the profile';
            public       postgres    false    233            m           0    0 7   COLUMN tb_profile_characteristics.c_profile_scenario_pk    COMMENT     i   COMMENT ON COLUMN public.tb_profile_characteristics.c_profile_scenario_pk IS 'Description of scenario ';
            public       postgres    false    233            n           0    0 =   COLUMN tb_profile_characteristics.c_profile_reference_year_pk    COMMENT     u   COMMENT ON COLUMN public.tb_profile_characteristics.c_profile_reference_year_pk IS 'reference year for the profile';
            public       postgres    false    233            o           0    0 E   COLUMN tb_profile_characteristics.c_profile_characteristrics_type_pfk    COMMENT     {   COMMENT ON COLUMN public.tb_profile_characteristics.c_profile_characteristrics_type_pfk IS 'abbreviation of profile type';
            public       postgres    false    233            p           0    0 6   COLUMN tb_profile_characteristics.c_profile_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_profile_characteristics.c_profile_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       postgres    false    233            q           0    0     TABLE tb_profile_characteristics    ACL     �   GRANT ALL ON TABLE public.tb_profile_characteristics TO sozio_e2s_admin_role;
GRANT SELECT ON TABLE public.tb_profile_characteristics TO "ENTIGRIS_read_only_role";
            public       postgres    false    233            �            1259    239665    tb_profile_types    TABLE     *  CREATE TABLE public.tb_profile_types (
    c_profile_type_pk character varying NOT NULL,
    c_profile_type_description character varying NOT NULL,
    c_profile_type_comment character varying,
    c_profile_type_last_modified date NOT NULL,
    c_profile_type_editor character varying NOT NULL
);
 $   DROP TABLE public.tb_profile_types;
       public         postgres    false            r           0    0    TABLE tb_profile_types    COMMENT     G   COMMENT ON TABLE public.tb_profile_types IS 'Lists all profile types';
            public       postgres    false    234            s           0    0 )   COLUMN tb_profile_types.c_profile_type_pk    COMMENT     _   COMMENT ON COLUMN public.tb_profile_types.c_profile_type_pk IS 'abbreviation of profile type';
            public       postgres    false    234            t           0    0    TABLE tb_profile_types    ACL     �   GRANT ALL ON TABLE public.tb_profile_types TO sozio_e2s_admin_role;
GRANT SELECT ON TABLE public.tb_profile_types TO "ENTIGRIS_read_only_role";
            public       postgres    false    234            �            1259    239671    tb_profiles    TABLE       CREATE TABLE public.tb_profiles (
    c_profiles_profile_pfk character varying NOT NULL,
    c_profiles_profile_scenario_pfk character varying NOT NULL,
    c_profiles_profile_reference_year_pfk integer NOT NULL,
    c_profiles_profile_characteristrics_type_pfk character varying NOT NULL,
    c_profiles_timestamp_pk timestamp with time zone NOT NULL,
    c_profiles_value numeric NOT NULL,
    c_profiles_units_fk character varying NOT NULL,
    c_profiles_last_modified date NOT NULL,
    c_profiles_editor character varying NOT NULL
);
    DROP TABLE public.tb_profiles;
       public         postgres    false            u           0    0    TABLE tb_profiles    COMMENT     P   COMMENT ON TABLE public.tb_profiles IS 'table contains profiles per timestamp';
            public       postgres    false    235            v           0    0 )   COLUMN tb_profiles.c_profiles_profile_pfk    COMMENT     c   COMMENT ON COLUMN public.tb_profiles.c_profiles_profile_pfk IS 'unique identifier of the profile';
            public       postgres    false    235            w           0    0 2   COLUMN tb_profiles.c_profiles_profile_scenario_pfk    COMMENT     c   COMMENT ON COLUMN public.tb_profiles.c_profiles_profile_scenario_pfk IS 'Description of scenario';
            public       postgres    false    235            x           0    0 8   COLUMN tb_profiles.c_profiles_profile_reference_year_pfk    COMMENT     p   COMMENT ON COLUMN public.tb_profiles.c_profiles_profile_reference_year_pfk IS 'reference year for the profile';
            public       postgres    false    235            y           0    0 ?   COLUMN tb_profiles.c_profiles_profile_characteristrics_type_pfk    COMMENT     u   COMMENT ON COLUMN public.tb_profiles.c_profiles_profile_characteristrics_type_pfk IS 'abbreviation of profile type';
            public       postgres    false    235            z           0    0    TABLE tb_profiles    ACL     �   GRANT ALL ON TABLE public.tb_profiles TO sozio_e2s_admin_role;
GRANT SELECT ON TABLE public.tb_profiles TO "ENTIGRIS_read_only_role";
            public       postgres    false    235            �            1259    239677    tb_regional_level    TABLE     �   CREATE TABLE public.tb_regional_level (
    c_regional_level_pk character varying NOT NULL,
    c_regional_level_comment character varying,
    c_regional_level_last_modified date NOT NULL,
    c_regional_level_editor character varying NOT NULL
);
 %   DROP TABLE public.tb_regional_level;
       public         sozio_e2s_admin_role    false            {           0    0    TABLE tb_regional_level    COMMENT     S   COMMENT ON TABLE public.tb_regional_level IS 'describes the regional resolutions';
            public       sozio_e2s_admin_role    false    236            |           0    0    TABLE tb_regional_level    ACL     G   GRANT SELECT ON TABLE public.tb_regional_level TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    236            �            1259    239408 
   tb_regions    TABLE     �  CREATE TABLE public.tb_regions (
    c_regions_pk character varying NOT NULL,
    c_regions_name character varying NOT NULL,
    c_regions_level character varying NOT NULL,
    c_regions_sources_fk character varying NOT NULL,
    c_regions_comment character varying,
    c_regions_quality integer NOT NULL,
    c_regions_geometry public.geometry(MultiPolygon,3044) NOT NULL,
    c_regions_last_modification character varying NOT NULL,
    c_regions_editor character varying NOT NULL
);
    DROP TABLE public.tb_regions;
       public         sozio_e2s_admin_role    false    2    2    2    2    2    2    2    2            }           0    0    TABLE tb_regions    COMMENT     �   COMMENT ON TABLE public.tb_regions IS 'tabel contains an overview on all regions, containing the shape information for each level - serves as a parent table';
            public       sozio_e2s_admin_role    false    201            ~           0    0    COLUMN tb_regions.c_regions_pk    COMMENT     �   COMMENT ON COLUMN public.tb_regions.c_regions_pk IS 'refers to NUTS nomenclature (e.g. germany = DE, Baden-Würtemberg = DE1)';
            public       sozio_e2s_admin_role    false    201                       0    0     COLUMN tb_regions.c_regions_name    COMMENT     �   COMMENT ON COLUMN public.tb_regions.c_regions_name IS '"Deutschland", "Mittelfranken", etc.. corresonsding to NUTS3 nomenclature';
            public       sozio_e2s_admin_role    false    201            �           0    0 !   COLUMN tb_regions.c_regions_level    COMMENT     �   COMMENT ON COLUMN public.tb_regions.c_regions_level IS 'level 0 -> country
level 1 -> federal state
level 2 -> NUTS3
!!! Constraint needed';
            public       sozio_e2s_admin_role    false    201            �           0    0 &   COLUMN tb_regions.c_regions_sources_fk    COMMENT     x   COMMENT ON COLUMN public.tb_regions.c_regions_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    201            �           0    0 #   COLUMN tb_regions.c_regions_comment    COMMENT     O   COMMENT ON COLUMN public.tb_regions.c_regions_comment IS 'comment on regions';
            public       sozio_e2s_admin_role    false    201            �           0    0 #   COLUMN tb_regions.c_regions_quality    COMMENT     �   COMMENT ON COLUMN public.tb_regions.c_regions_quality IS '1 -> related to citable source; 2 -> very good guessed assumption; 3 -> assumption';
            public       sozio_e2s_admin_role    false    201            �           0    0 $   COLUMN tb_regions.c_regions_geometry    COMMENT     �   COMMENT ON COLUMN public.tb_regions.c_regions_geometry IS 'geometry key: processed by using this skript... 
Datatype: geometry (MultiPolygon, 3044)';
            public       sozio_e2s_admin_role    false    201            �           0    0    TABLE tb_regions    ACL     @   GRANT SELECT ON TABLE public.tb_regions TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    201            �            1259    239683    tb_relation_fuels_technologies    TABLE       CREATE TABLE public.tb_relation_fuels_technologies (
    c_technology_pfk character varying NOT NULL,
    c_fuels_pfk character varying NOT NULL,
    c_relation_fuels_technologies_last_modified date NOT NULL,
    c_relation_fuels_technologies_editor character varying NOT NULL
);
 2   DROP TABLE public.tb_relation_fuels_technologies;
       public         sozio_e2s_admin_role    false            �           0    0 $   TABLE tb_relation_fuels_technologies    COMMENT     |   COMMENT ON TABLE public.tb_relation_fuels_technologies IS 'tabel contains the relation between the technologies and fuels';
            public       sozio_e2s_admin_role    false    237            �           0    0 6   COLUMN tb_relation_fuels_technologies.c_technology_pfk    COMMENT     h   COMMENT ON COLUMN public.tb_relation_fuels_technologies.c_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    237            �           0    0 1   COLUMN tb_relation_fuels_technologies.c_fuels_pfk    COMMENT     e   COMMENT ON COLUMN public.tb_relation_fuels_technologies.c_fuels_pfk IS 'table containing all fuels';
            public       sozio_e2s_admin_role    false    237            �           0    0 Q   COLUMN tb_relation_fuels_technologies.c_relation_fuels_technologies_last_modified    COMMENT     �   COMMENT ON COLUMN public.tb_relation_fuels_technologies.c_relation_fuels_technologies_last_modified IS '!!! Trigger date of upload';
            public       sozio_e2s_admin_role    false    237            �           0    0 $   TABLE tb_relation_fuels_technologies    ACL     T   GRANT SELECT ON TABLE public.tb_relation_fuels_technologies TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    237            �            1259    239689 *   tb_relation_investment_option_alternatives    TABLE     �  CREATE TABLE public.tb_relation_investment_option_alternatives (
    c_rel_inv_op_altern_technology_pfk character varying NOT NULL,
    c_rel_inv_op_altern_investment_option_size_pfk int4range NOT NULL,
    c_rel_inv_op_altern_investment_option_size_units_pfk character varying NOT NULL,
    c_rel_inv_op_altern_sub_technology_pfk character varying NOT NULL,
    c_rel_inv_op_altern_comment character varying,
    c_rel_inv_op_altern_quality character varying NOT NULL,
    c_rel_inv_op_altern_sources_fk character varying,
    c_rel_inv_op_altern_last_modification date NOT NULL,
    c_rel_inv_op_altern_editor character varying NOT NULL
);
 >   DROP TABLE public.tb_relation_investment_option_alternatives;
       public         sozio_e2s_admin_role    false            �           0    0 0   TABLE tb_relation_investment_option_alternatives    COMMENT     �   COMMENT ON TABLE public.tb_relation_investment_option_alternatives IS 'Identifies the relation between one investment option and its alternatives';
            public       sozio_e2s_admin_role    false    238            �           0    0 T   COLUMN tb_relation_investment_option_alternatives.c_rel_inv_op_altern_technology_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_relation_investment_option_alternatives.c_rel_inv_op_altern_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    238            �           0    0 `   COLUMN tb_relation_investment_option_alternatives.c_rel_inv_op_altern_investment_option_size_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_relation_investment_option_alternatives.c_rel_inv_op_altern_investment_option_size_pfk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       sozio_e2s_admin_role    false    238            �           0    0 X   COLUMN tb_relation_investment_option_alternatives.c_rel_inv_op_altern_sub_technology_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_relation_investment_option_alternatives.c_rel_inv_op_altern_sub_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    238            �           0    0 P   COLUMN tb_relation_investment_option_alternatives.c_rel_inv_op_altern_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_relation_investment_option_alternatives.c_rel_inv_op_altern_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    238            �            1259    239695 )   tb_relation_investment_option_application    TABLE     �  CREATE TABLE public.tb_relation_investment_option_application (
    c_application_pfk character varying NOT NULL,
    c_technology_pfk character varying NOT NULL,
    c_investment_options_size_pk int4range NOT NULL,
    c_investment_options_units_pfk character varying NOT NULL,
    c_relation_application_investment_option_comment character varying,
    c_relation_application_investment_option_editor character varying NOT NULL,
    c_relation_application_investment_option_last_modification date NOT NULL
);
 =   DROP TABLE public.tb_relation_investment_option_application;
       public         sozio_e2s_admin_role    false            �           0    0 B   COLUMN tb_relation_investment_option_application.c_application_pfk    COMMENT     l   COMMENT ON COLUMN public.tb_relation_investment_option_application.c_application_pfk IS 'app_1, app_2, ..';
            public       sozio_e2s_admin_role    false    239            �           0    0 A   COLUMN tb_relation_investment_option_application.c_technology_pfk    COMMENT     s   COMMENT ON COLUMN public.tb_relation_investment_option_application.c_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    239            �           0    0 M   COLUMN tb_relation_investment_option_application.c_investment_options_size_pk    COMMENT     �   COMMENT ON COLUMN public.tb_relation_investment_option_application.c_investment_options_size_pk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       sozio_e2s_admin_role    false    239            �           0    0 /   TABLE tb_relation_investment_option_application    ACL     _   GRANT SELECT ON TABLE public.tb_relation_investment_option_application TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    239            �            1259    239701    tb_relation_investor    TABLE     M  CREATE TABLE public.tb_relation_investor (
    c_relation_investor_main_pfk character varying NOT NULL,
    c_relation_investor_sub_pfk character varying NOT NULL,
    c_relation_investor_last_modification date NOT NULL,
    c_relation_investor_comment character varying,
    c_relation_investor_editor character varying NOT NULL
);
 (   DROP TABLE public.tb_relation_investor;
       public         sozio_e2s_admin_role    false            �           0    0 7   COLUMN tb_relation_investor.c_relation_investor_sub_pfk    COMMENT     }   COMMENT ON COLUMN public.tb_relation_investor.c_relation_investor_sub_pfk IS 'investor key (private = priv, evu = EVU,...)';
            public       sozio_e2s_admin_role    false    240            �           0    0    TABLE tb_relation_investor    ACL     J   GRANT SELECT ON TABLE public.tb_relation_investor TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    240            �            1259    239707 &   tb_relation_investor_investment_option    TABLE     C  CREATE TABLE public.tb_relation_investor_investment_option (
    c_technology_pfk character varying NOT NULL,
    c_investment_options_size_pfk int4range NOT NULL,
    c_investment_options_units_pfk character varying NOT NULL,
    c_investors_pfk character varying NOT NULL,
    c_relation_investor_investment_option_quality integer NOT NULL,
    c_relation_investor_investment_option_comment character varying,
    c_relation_investor_investment_option_last_modification character varying NOT NULL,
    c_relation_investor_investment_option_editor character varying NOT NULL
);
 :   DROP TABLE public.tb_relation_investor_investment_option;
       public         sozio_e2s_admin_role    false            �           0    0 >   COLUMN tb_relation_investor_investment_option.c_technology_pfk    COMMENT     p   COMMENT ON COLUMN public.tb_relation_investor_investment_option.c_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    241            �           0    0 K   COLUMN tb_relation_investor_investment_option.c_investment_options_size_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_relation_investor_investment_option.c_investment_options_size_pfk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       sozio_e2s_admin_role    false    241            �           0    0 =   COLUMN tb_relation_investor_investment_option.c_investors_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_relation_investor_investment_option.c_investors_pfk IS 'investor key (private = priv, evu = EVU,...)';
            public       sozio_e2s_admin_role    false    241            �           0    0 ,   TABLE tb_relation_investor_investment_option    ACL     \   GRANT SELECT ON TABLE public.tb_relation_investor_investment_option TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    241            �            1259    239713     tb_relation_regional_level_stock    TABLE     H  CREATE TABLE public.tb_relation_regional_level_stock (
    c_regional_coverage_pfk character varying NOT NULL,
    c_regional_level_pfk character varying NOT NULL,
    c_stock_scenario_pfk character varying NOT NULL,
    c_comment character varying,
    c_last_modified date NOT NULL,
    c_editor character varying NOT NULL
);
 4   DROP TABLE public.tb_relation_regional_level_stock;
       public         sozio_e2s_admin_role    false            �           0    0 &   TABLE tb_relation_regional_level_stock    COMMENT     �   COMMENT ON TABLE public.tb_relation_regional_level_stock IS 'Contains the relation between the regional level of the stock data and the dataset in tb_stock';
            public       sozio_e2s_admin_role    false    242            �           0    0 ?   COLUMN tb_relation_regional_level_stock.c_regional_coverage_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_relation_regional_level_stock.c_regional_coverage_pfk IS 'refers to NUTS nomenclature (e.g. germany = DE, Baden-Würtemberg = DE1)';
            public       sozio_e2s_admin_role    false    242            �           0    0 &   TABLE tb_relation_regional_level_stock    ACL     V   GRANT SELECT ON TABLE public.tb_relation_regional_level_stock TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    242            �            1259    239719    tb_relation_regions    TABLE       CREATE TABLE public.tb_relation_regions (
    c_regions_main_pfk character varying NOT NULL,
    c_regions_sub_pfk character varying NOT NULL,
    c_relation_regions_last_modification date NOT NULL,
    c_relation_regions_editor character varying NOT NULL
);
 '   DROP TABLE public.tb_relation_regions;
       public         sozio_e2s_admin_role    false            �           0    0 -   COLUMN tb_relation_regions.c_regions_main_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_relation_regions.c_regions_main_pfk IS 'refers to NUTS nomenclature (e.g. germany = DE, Baden-Würtemberg = DE1)';
            public       sozio_e2s_admin_role    false    243            �           0    0 ,   COLUMN tb_relation_regions.c_regions_sub_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_relation_regions.c_regions_sub_pfk IS 'refers to NUTS nomenclature (e.g. germany = DE, Baden-Würtemberg = DE1)';
            public       sozio_e2s_admin_role    false    243            �           0    0    TABLE tb_relation_regions    ACL     I   GRANT SELECT ON TABLE public.tb_relation_regions TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    243            �            1259    239725    tb_relation_technologies    TABLE       CREATE TABLE public.tb_relation_technologies (
    c_technology_main_pfk character varying NOT NULL,
    c_technology_sub_pfk character varying NOT NULL,
    c_relation_technologies_last_modification date NOT NULL,
    c_relation_technologies_editor character varying NOT NULL
);
 ,   DROP TABLE public.tb_relation_technologies;
       public         sozio_e2s_admin_role    false            �           0    0    TABLE tb_relation_technologies    COMMENT     r   COMMENT ON TABLE public.tb_relation_technologies IS 'Relation table between main technologies and subtechnology';
            public       sozio_e2s_admin_role    false    244            �           0    0 5   COLUMN tb_relation_technologies.c_technology_main_pfk    COMMENT     g   COMMENT ON COLUMN public.tb_relation_technologies.c_technology_main_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    244            �           0    0 4   COLUMN tb_relation_technologies.c_technology_sub_pfk    COMMENT     f   COMMENT ON COLUMN public.tb_relation_technologies.c_technology_sub_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    244            �           0    0    TABLE tb_relation_technologies    ACL     N   GRANT SELECT ON TABLE public.tb_relation_technologies TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    244            �            1259    239731    tb_respondends    TABLE       CREATE TABLE public.tb_respondends (
    c_respondend_pk character varying NOT NULL,
    c_respondend_comment character varying NOT NULL,
    c_respondend_last_modified date NOT NULL,
    c_respondend_editor character varying NOT NULL,
    c_respondend_weight numeric
);
 "   DROP TABLE public.tb_respondends;
       public         sozio_e2s_admin_role    false            �           0    0    TABLE tb_respondends    ACL     D   GRANT SELECT ON TABLE public.tb_respondends TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    245            �            1259    239737    tb_respondends_sub_groups    TABLE     �  CREATE TABLE public.tb_respondends_sub_groups (
    c_respondends_sub_groups_main_group_pk character varying NOT NULL,
    c_respondends_sub_groups_sub_group_pk character varying NOT NULL,
    c_respondends_sub_groups_respondend_pfk character varying NOT NULL,
    c_respondends_sub_groups_technology_pfk character varying NOT NULL,
    c_respondends_sub_groups_comment character varying,
    c_respondends_sub_groups_quality character varying NOT NULL,
    c_respondends_sub_groups_sources_fk character varying,
    c_respondends_sub_groups_last_modification date NOT NULL,
    c_respondends_sub_groups_editor character varying NOT NULL
);
 -   DROP TABLE public.tb_respondends_sub_groups;
       public         postgres    false            �           0    0    TABLE tb_respondends_sub_groups    COMMENT     t   COMMENT ON TABLE public.tb_respondends_sub_groups IS 'Categorisation of respondends from soziotrend market survey';
            public       postgres    false    246            �           0    0 G   COLUMN tb_respondends_sub_groups.c_respondends_sub_groups_main_group_pk    COMMENT     �   COMMENT ON COLUMN public.tb_respondends_sub_groups.c_respondends_sub_groups_main_group_pk IS 'Main group category (e.g. environmental NGO)';
            public       postgres    false    246            �           0    0 H   COLUMN tb_respondends_sub_groups.c_respondends_sub_groups_technology_pfk    COMMENT     z   COMMENT ON COLUMN public.tb_respondends_sub_groups.c_respondends_sub_groups_technology_pfk IS 'abbr. of technology name';
            public       postgres    false    246            �           0    0 D   COLUMN tb_respondends_sub_groups.c_respondends_sub_groups_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_respondends_sub_groups.c_respondends_sub_groups_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       postgres    false    246            �           0    0    TABLE tb_respondends_sub_groups    ACL     M   GRANT ALL ON TABLE public.tb_respondends_sub_groups TO sozio_e2s_admin_role;
            public       postgres    false    246            �            1259    239743 
   tb_sources    TABLE     �  CREATE TABLE public.tb_sources (
    c_sources_pk character varying NOT NULL,
    c_sources_author character varying NOT NULL,
    c_sources_title character varying NOT NULL,
    c_sources_publication_year character varying NOT NULL,
    c_sources_location character varying NOT NULL,
    c_sources_publisher character varying NOT NULL,
    c_sources_url character varying,
    c_sources_page integer,
    c_sources_licence character varying,
    c_sources_copyright character varying,
    c_sources_quality integer NOT NULL,
    c_sources_comment character varying,
    c_sources_last_modification character varying NOT NULL,
    c_sources_editor character varying NOT NULL
);
    DROP TABLE public.tb_sources;
       public         sozio_e2s_admin_role    false            �           0    0    TABLE tb_sources    COMMENT     |   COMMENT ON TABLE public.tb_sources IS 'tabel contains an overview on all sources that are used - serves as a parent table';
            public       sozio_e2s_admin_role    false    247            �           0    0    COLUMN tb_sources.c_sources_pk    COMMENT     p   COMMENT ON COLUMN public.tb_sources.c_sources_pk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    247            �           0    0 !   COLUMN tb_sources.c_sources_title    COMMENT     L   COMMENT ON COLUMN public.tb_sources.c_sources_title IS 'title of document';
            public       sozio_e2s_admin_role    false    247            �           0    0 $   COLUMN tb_sources.c_sources_location    COMMENT     U   COMMENT ON COLUMN public.tb_sources.c_sources_location IS 'location of publication';
            public       sozio_e2s_admin_role    false    247            �           0    0 %   COLUMN tb_sources.c_sources_publisher    COMMENT     X   COMMENT ON COLUMN public.tb_sources.c_sources_publisher IS 'publisher of the document';
            public       sozio_e2s_admin_role    false    247            �           0    0    COLUMN tb_sources.c_sources_url    COMMENT     H   COMMENT ON COLUMN public.tb_sources.c_sources_url IS 'URL of document';
            public       sozio_e2s_admin_role    false    247            �           0    0 #   COLUMN tb_sources.c_sources_quality    COMMENT     �   COMMENT ON COLUMN public.tb_sources.c_sources_quality IS '1 -> related to citable source; 2 -> very good guessed assumption; 3 -> assumption';
            public       sozio_e2s_admin_role    false    247            �           0    0 #   COLUMN tb_sources.c_sources_comment    COMMENT     l   COMMENT ON COLUMN public.tb_sources.c_sources_comment IS 'comment on source (e.g. assumption is that,...)';
            public       sozio_e2s_admin_role    false    247            �           0    0 "   COLUMN tb_sources.c_sources_editor    COMMENT     P   COMMENT ON COLUMN public.tb_sources.c_sources_editor IS 'editor of data entry';
            public       sozio_e2s_admin_role    false    247            �           0    0    TABLE tb_sources    ACL     @   GRANT SELECT ON TABLE public.tb_sources TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    247            �            1259    239749    tb_specific_consumption    TABLE     b  CREATE TABLE public.tb_specific_consumption (
    c_specific_consumption_year integer NOT NULL,
    c_specific_consumption_technology_pfk character varying NOT NULL,
    c_specific_consumption_sub_technology_pfk character varying NOT NULL,
    c_specific_consumption_investment_options_size_pfk int4range NOT NULL,
    c_specific_consumption_investment_options_units_pfk character varying NOT NULL,
    c_specific_consumption_scenario character varying NOT NULL,
    c_specific_consumption_value numeric NOT NULL,
    c_specific_consumption_units_fk character varying NOT NULL,
    c_specific_consumption_comment character varying,
    c_specific_consumption_quality integer NOT NULL,
    c_specific_consumption_sources_fk character varying,
    c_specific_consumption_last_modification date NOT NULL,
    c_specific_consumption_editor character varying NOT NULL
);
 +   DROP TABLE public.tb_specific_consumption;
       public         postgres    false            �           0    0    TABLE tb_specific_consumption    COMMENT     T   COMMENT ON TABLE public.tb_specific_consumption IS 'specific consumption of cars ';
            public       postgres    false    248            �           0    0 D   COLUMN tb_specific_consumption.c_specific_consumption_technology_pfk    COMMENT     v   COMMENT ON COLUMN public.tb_specific_consumption.c_specific_consumption_technology_pfk IS 'abbr. of technology name';
            public       postgres    false    248            �           0    0 H   COLUMN tb_specific_consumption.c_specific_consumption_sub_technology_pfk    COMMENT     z   COMMENT ON COLUMN public.tb_specific_consumption.c_specific_consumption_sub_technology_pfk IS 'abbr. of technology name';
            public       postgres    false    248            �           0    0 Q   COLUMN tb_specific_consumption.c_specific_consumption_investment_options_size_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_specific_consumption.c_specific_consumption_investment_options_size_pfk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       postgres    false    248            �           0    0 @   COLUMN tb_specific_consumption.c_specific_consumption_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_specific_consumption.c_specific_consumption_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       postgres    false    248            �           0    0    TABLE tb_specific_consumption    ACL     K   GRANT ALL ON TABLE public.tb_specific_consumption TO sozio_e2s_admin_role;
            public       postgres    false    248            �            1259    239755    tb_specific_emissions_cv    TABLE       CREATE TABLE public.tb_specific_emissions_cv (
    c_specific_emissions_construction_year_pk integer NOT NULL,
    c_specific_emissions_technology_pfk character varying NOT NULL,
    c_specific_emissions_investment_options_size_pk int4range NOT NULL,
    c_specific_emissions_investment_options_units_pfk character varying NOT NULL,
    c_specific_emissions_scenario_pk character varying NOT NULL,
    c_specific_emissions_value integer NOT NULL,
    c_specific_emissions_units_fk character varying NOT NULL,
    c_specific_emissions_comment character varying,
    c_specific_emissions_quality integer NOT NULL,
    c_specific_emissions_sources_fk character varying,
    c_specific_emissions_last_modification date NOT NULL,
    c_specific_emissions_editor character varying NOT NULL
);
 ,   DROP TABLE public.tb_specific_emissions_cv;
       public         postgres    false            �           0    0    TABLE tb_specific_emissions_cv    COMMENT     �   COMMENT ON TABLE public.tb_specific_emissions_cv IS 'Contains the specific emissions of conventional vehicles according to the size of the car';
            public       postgres    false    249            �           0    0 C   COLUMN tb_specific_emissions_cv.c_specific_emissions_technology_pfk    COMMENT     u   COMMENT ON COLUMN public.tb_specific_emissions_cv.c_specific_emissions_technology_pfk IS 'abbr. of technology name';
            public       postgres    false    249            �           0    0 O   COLUMN tb_specific_emissions_cv.c_specific_emissions_investment_options_size_pk    COMMENT     �   COMMENT ON COLUMN public.tb_specific_emissions_cv.c_specific_emissions_investment_options_size_pk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       postgres    false    249            �           0    0 ?   COLUMN tb_specific_emissions_cv.c_specific_emissions_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_specific_emissions_cv.c_specific_emissions_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       postgres    false    249            �           0    0    TABLE tb_specific_emissions_cv    ACL     L   GRANT ALL ON TABLE public.tb_specific_emissions_cv TO sozio_e2s_admin_role;
            public       postgres    false    249            �            1259    239761 %   tb_specific_emissions_electricity_mix    TABLE     �  CREATE TABLE public.tb_specific_emissions_electricity_mix (
    c_specific_emissions_electricity_mix_year integer NOT NULL,
    c_specific_emissions_electricity_mix_scenario character varying NOT NULL,
    c_specific_emissions_electricity_mix_value numeric NOT NULL,
    c_specific_emissions_electricity_mix_units_fk character varying NOT NULL,
    c_specific_emissions_electricity_mix_comment character varying,
    c_specific_emissions_electricity_mix_quality integer NOT NULL,
    c_specific_emissions_electricity_mix_sources_fk character varying,
    c_specific_emissions_electricity_mix_last_modification date NOT NULL,
    c_specific_emissions_electricity_mix_editor character varying NOT NULL
);
 9   DROP TABLE public.tb_specific_emissions_electricity_mix;
       public         postgres    false            �           0    0 +   TABLE tb_specific_emissions_electricity_mix    COMMENT     y   COMMENT ON TABLE public.tb_specific_emissions_electricity_mix IS 'specific emissions of the electricity mix 2018- 2050';
            public       postgres    false    250            �           0    0 \   COLUMN tb_specific_emissions_electricity_mix.c_specific_emissions_electricity_mix_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_specific_emissions_electricity_mix.c_specific_emissions_electricity_mix_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       postgres    false    250            �           0    0 +   TABLE tb_specific_emissions_electricity_mix    ACL     Y   GRANT ALL ON TABLE public.tb_specific_emissions_electricity_mix TO sozio_e2s_admin_role;
            public       postgres    false    250            �            1259    239767    tb_stock_bat    TABLE     K  CREATE TABLE public.tb_stock_bat (
    c_stock_bat_technology_pfk character varying NOT NULL,
    c_stock_bat_regions_pfk character varying NOT NULL,
    c_stock_bat_initial_operation_pk integer NOT NULL,
    c_stock_bat_scenario_pk character varying NOT NULL,
    c_stock_bat_value numeric NOT NULL,
    c_stock_bat_units_fk character varying NOT NULL,
    c_stock_bat_comment character varying,
    c_stock_bat_quality integer NOT NULL,
    c_stock_bat_sources_fk character varying,
    c_stock_bat_last_modification date NOT NULL,
    c_stock_bat_editor character varying NOT NULL
);
     DROP TABLE public.tb_stock_bat;
       public         postgres    false            �           0    0 .   COLUMN tb_stock_bat.c_stock_bat_technology_pfk    COMMENT     `   COMMENT ON COLUMN public.tb_stock_bat.c_stock_bat_technology_pfk IS 'abbr. of technology name';
            public       postgres    false    251            �           0    0 +   COLUMN tb_stock_bat.c_stock_bat_regions_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_stock_bat.c_stock_bat_regions_pfk IS 'refers to NUTS nomenclature (e.g. germany = DE, Baden-Würtemberg = DE1)';
            public       postgres    false    251            �           0    0 *   COLUMN tb_stock_bat.c_stock_bat_sources_fk    COMMENT     |   COMMENT ON COLUMN public.tb_stock_bat.c_stock_bat_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       postgres    false    251            �           0    0    TABLE tb_stock_bat    ACL     @   GRANT ALL ON TABLE public.tb_stock_bat TO sozio_e2s_admin_role;
            public       postgres    false    251            �            1259    239773    tb_stock_parameter    TABLE     
  CREATE TABLE public.tb_stock_parameter (
    c_stock_parameter_pk character varying NOT NULL,
    c_stock_parameter_description character varying NOT NULL,
    c_stock_parameter_last_modified date NOT NULL,
    c_stock_parameter_editor character varying NOT NULL
);
 &   DROP TABLE public.tb_stock_parameter;
       public         sozio_e2s_admin_role    false            �           0    0    TABLE tb_stock_parameter    COMMENT     z   COMMENT ON TABLE public.tb_stock_parameter IS 'stock parameter (number of systems; installed_capacity; installed_power)';
            public       sozio_e2s_admin_role    false    252            �           0    0    TABLE tb_stock_parameter    ACL     H   GRANT SELECT ON TABLE public.tb_stock_parameter TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    252            �            1259    239779    tb_stock_pv    TABLE     �  CREATE TABLE public.tb_stock_pv (
    c_stock_pv_technology_pfk character varying NOT NULL,
    c_stock_pv_id_pk character varying NOT NULL,
    c_stock_pv_regions_nuts3_pfk character varying NOT NULL,
    c_stock_pv_regions_federal_pfk character varying,
    c_stock_pv_regions_national_pfk character varying,
    c_stock_pv_value numeric NOT NULL,
    c_stock_pv_units_fk character varying NOT NULL,
    c_stock_pv_scenario character varying NOT NULL,
    c_stock_pv_initial_operation integer,
    c_stock_pv_decommissioning integer,
    c_stock_pv_subsidized boolean,
    c_stock_pv_fit_levy boolean,
    c_stock_pv_status_fk character varying,
    c_stock_pv_grid_level_fk character varying,
    c_stock_pv_postcode character varying,
    c_stock_pv_comment character varying,
    c_stock_pv_sources_fk character varying,
    c_stock_pv_quality integer NOT NULL,
    c_stock_pv_last_modified date NOT NULL,
    c_stock_pv_editor character varying NOT NULL,
    c_stock_pv_application_fk character varying
);
    DROP TABLE public.tb_stock_pv;
       public         sozio_e2s_admin_role    false            �           0    0    TABLE tb_stock_pv    ACL     A   GRANT SELECT ON TABLE public.tb_stock_pv TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    253            �            1259    239785    tb_stock_scenario    TABLE     �   CREATE TABLE public.tb_stock_scenario (
    tb_stock_scenario_pk character varying NOT NULL,
    c_stock_scenario_comment character varying,
    c_stock_scenario_last_modified date NOT NULL,
    c_stock_scenario_editor character varying NOT NULL
);
 %   DROP TABLE public.tb_stock_scenario;
       public         sozio_e2s_admin_role    false            �           0    0    TABLE tb_stock_scenario    COMMENT     W   COMMENT ON TABLE public.tb_stock_scenario IS 'defines the scenario of the stock data';
            public       sozio_e2s_admin_role    false    254            �           0    0    TABLE tb_stock_scenario    ACL     G   GRANT SELECT ON TABLE public.tb_stock_scenario TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    254            �            1259    239791    tb_sub_technology_shares    TABLE     �  CREATE TABLE public.tb_sub_technology_shares (
    c_sub_tec_shares_technology_pfk character varying NOT NULL,
    c_sub_tec_shares_validity_year integer NOT NULL,
    c_sub_tec_shares_value numeric NOT NULL,
    c_sub_tec_shares_units_fk character varying,
    c_sub_tec_shares_sources_fk character varying,
    c_sub_tec_shares_comment character varying,
    c_sub_tec_shares_qualiy integer NOT NULL,
    c_sub_tec_shares_last_modified date NOT NULL,
    c_sub_tec_shares_editor character varying NOT NULL
);
 ,   DROP TABLE public.tb_sub_technology_shares;
       public         postgres    false            �           0    0    TABLE tb_sub_technology_shares    COMMENT     Q   COMMENT ON TABLE public.tb_sub_technology_shares IS 'shares of subtechnologies';
            public       postgres    false    255            �           0    0 ?   COLUMN tb_sub_technology_shares.c_sub_tec_shares_technology_pfk    COMMENT     q   COMMENT ON COLUMN public.tb_sub_technology_shares.c_sub_tec_shares_technology_pfk IS 'abbr. of technology name';
            public       postgres    false    255            �           0    0 ;   COLUMN tb_sub_technology_shares.c_sub_tec_shares_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_sub_technology_shares.c_sub_tec_shares_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       postgres    false    255            �           0    0    TABLE tb_sub_technology_shares    ACL     L   GRANT ALL ON TABLE public.tb_sub_technology_shares TO sozio_e2s_admin_role;
            public       postgres    false    255                        1259    239797 "   tb_technical_characteristics_types    TABLE     ^  CREATE TABLE public.tb_technical_characteristics_types (
    c_technical_characteristics_types_pk character varying NOT NULL,
    c_technical_characteristics_types_description character varying NOT NULL,
    c_technical_characteristics_types_last_modification date NOT NULL,
    c_technical_characteristics_types_editor character varying NOT NULL
);
 6   DROP TABLE public.tb_technical_characteristics_types;
       public         sozio_e2s_admin_role    false            �           0    0 (   TABLE tb_technical_characteristics_types    COMMENT     �   COMMENT ON TABLE public.tb_technical_characteristics_types IS 'tabel contains an overview on all types of technical characteristics that are used - serves as a parent table';
            public       sozio_e2s_admin_role    false    256            �           0    0 (   TABLE tb_technical_characteristics_types    ACL     X   GRANT SELECT ON TABLE public.tb_technical_characteristics_types TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    256                       1259    239803    tb_technologies    TABLE        CREATE TABLE public.tb_technologies (
    c_technology_pk character varying NOT NULL,
    c_technologies_name character varying NOT NULL,
    c_technologies_comment character varying,
    c_technologies_last_modified date NOT NULL,
    c_technologies_editor character varying NOT NULL
);
 #   DROP TABLE public.tb_technologies;
       public         sozio_e2s_admin_role    false            �           0    0    TABLE tb_technologies    COMMENT     �   COMMENT ON TABLE public.tb_technologies IS 'tabel contains an overview on all technologies that are used - serves as a parent table';
            public       sozio_e2s_admin_role    false    257            �           0    0 &   COLUMN tb_technologies.c_technology_pk    COMMENT     X   COMMENT ON COLUMN public.tb_technologies.c_technology_pk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    257            �           0    0 *   COLUMN tb_technologies.c_technologies_name    COMMENT     �   COMMENT ON COLUMN public.tb_technologies.c_technologies_name IS 'name of the technology (e.g. wind, windOnshore, windOffshore, pv, pvRoof, etc.)';
            public       sozio_e2s_admin_role    false    257            �           0    0 -   COLUMN tb_technologies.c_technologies_comment    COMMENT     �   COMMENT ON COLUMN public.tb_technologies.c_technologies_comment IS 'comment on data entry; how was the assumption made; any nescessary information';
            public       sozio_e2s_admin_role    false    257            �           0    0 3   COLUMN tb_technologies.c_technologies_last_modified    COMMENT     g   COMMENT ON COLUMN public.tb_technologies.c_technologies_last_modified IS '!!! trigger date of upload';
            public       sozio_e2s_admin_role    false    257            �           0    0    TABLE tb_technologies    ACL     E   GRANT SELECT ON TABLE public.tb_technologies TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    257                       1259    239809    tb_technology_characteristics    TABLE     �  CREATE TABLE public.tb_technology_characteristics (
    c_technology_pfk character varying NOT NULL,
    c_technology_characteristics_types_pfk character varying NOT NULL,
    c_technology_characteristics_validity_period_pk daterange NOT NULL,
    c_technology_characteristics_value integer NOT NULL,
    c_technology_characteristics_units_fk character varying NOT NULL,
    c_technology_characteristics_quality integer NOT NULL,
    c_technology_characteristics_comment character varying NOT NULL,
    c_technology_characteristics_sources_fk character varying,
    c_technology_characteristics_last_modification character varying NOT NULL,
    c_technology_characteristics_editor character varying NOT NULL
);
 1   DROP TABLE public.tb_technology_characteristics;
       public         sozio_e2s_admin_role    false            �           0    0 #   TABLE tb_technology_characteristics    COMMENT     �   COMMENT ON TABLE public.tb_technology_characteristics IS 'tabel contains all values of technical characteristics in dependence of the technology and the validity year';
            public       sozio_e2s_admin_role    false    258            �           0    0 5   COLUMN tb_technology_characteristics.c_technology_pfk    COMMENT     g   COMMENT ON COLUMN public.tb_technology_characteristics.c_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    258            �           0    0 T   COLUMN tb_technology_characteristics.c_technology_characteristics_validity_period_pk    COMMENT     z   COMMENT ON COLUMN public.tb_technology_characteristics.c_technology_characteristics_validity_period_pk IS '!! daterange';
            public       sozio_e2s_admin_role    false    258            �           0    0 L   COLUMN tb_technology_characteristics.c_technology_characteristics_sources_fk    COMMENT     �   COMMENT ON COLUMN public.tb_technology_characteristics.c_technology_characteristics_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    258            �           0    0 #   TABLE tb_technology_characteristics    ACL     S   GRANT SELECT ON TABLE public.tb_technology_characteristics TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    258                       1259    239832    tb_units    TABLE       CREATE TABLE public.tb_units (
    c_units_pk character varying NOT NULL,
    c_units_abbreviation character varying NOT NULL,
    c_units_description character varying NOT NULL,
    c_units_last_modification character varying NOT NULL,
    c_units_editor character varying NOT NULL
);
    DROP TABLE public.tb_units;
       public         sozio_e2s_admin_role    false            �           0    0    TABLE tb_units    COMMENT     x   COMMENT ON TABLE public.tb_units IS 'tabel contains an overview on all units that are used - serves as a parent table';
            public       sozio_e2s_admin_role    false    259            �           0    0    TABLE tb_units    ACL     >   GRANT SELECT ON TABLE public.tb_units TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    259                       1259    239838    tb_utilities    TABLE     �  CREATE TABLE public.tb_utilities (
    c_utilities_attribute_pfk character varying NOT NULL,
    c_utilities_technology_pfk character varying NOT NULL,
    c_utilities_investment_options_size_pfk int4range NOT NULL,
    c_utilities_investment_options_units_pfk character varying NOT NULL,
    c_utilities_attribute_level_pfk character varying NOT NULL,
    c_utilities_respondend_pfk character varying NOT NULL,
    c_utilities_level_pk character varying NOT NULL,
    c_utilities_value numeric NOT NULL,
    c_utilities_comment character varying NOT NULL,
    c_utilities_quality character varying NOT NULL,
    c_utilities_sources_fk character varying NOT NULL,
    c_utilities_last_modification date NOT NULL,
    c_utilities_editor character varying NOT NULL
);
     DROP TABLE public.tb_utilities;
       public         sozio_e2s_admin_role    false            �           0    0 .   COLUMN tb_utilities.c_utilities_technology_pfk    COMMENT     `   COMMENT ON COLUMN public.tb_utilities.c_utilities_technology_pfk IS 'abbr. of technology name';
            public       sozio_e2s_admin_role    false    260            �           0    0 ;   COLUMN tb_utilities.c_utilities_investment_options_size_pfk    COMMENT     �   COMMENT ON COLUMN public.tb_utilities.c_utilities_investment_options_size_pfk IS 'for example 10 kW PV or 1 flotte, 1 car, 1 window...

!!!Datatype: Integer range';
            public       sozio_e2s_admin_role    false    260            �           0    0 *   COLUMN tb_utilities.c_utilities_sources_fk    COMMENT     |   COMMENT ON COLUMN public.tb_utilities.c_utilities_sources_fk IS 'primary key refers to bit tex keys using citavi database';
            public       sozio_e2s_admin_role    false    260            �           0    0    TABLE tb_utilities    ACL     B   GRANT SELECT ON TABLE public.tb_utilities TO sozio_e2s_read_role;
            public       sozio_e2s_admin_role    false    260            f           2606    240186 ?   tb_application_characteristics c_application_characteristics_pk 
   CONSTRAINT     ^  ALTER TABLE ONLY public.tb_application_characteristics
    ADD CONSTRAINT c_application_characteristics_pk PRIMARY KEY (c_technology_pfk, c_investment_options_size_pk, c_investment_options_units_pfk, c_application_characteristics_validity_time_pk, c_application_pfk, c_application_characteristics_scenario_pk, c_application_characteristic_types_pk);
 i   ALTER TABLE ONLY public.tb_application_characteristics DROP CONSTRAINT c_application_characteristics_pk;
       public         sozio_e2s_admin_role    false    204    204    204    204    204    204    204            d           2606    240188    tb_application c_application_pk 
   CONSTRAINT     k   ALTER TABLE ONLY public.tb_application
    ADD CONSTRAINT c_application_pk PRIMARY KEY (c_application_pk);
 I   ALTER TABLE ONLY public.tb_application DROP CONSTRAINT c_application_pk;
       public         sozio_e2s_admin_role    false    203            j           2606    240190 2   tb_attribute_level c_attribute_level_attribute_pfk 
   CONSTRAINT     $  ALTER TABLE ONLY public.tb_attribute_level
    ADD CONSTRAINT c_attribute_level_attribute_pfk PRIMARY KEY (c_attribute_level_attribute_pfk, c_attribute_level_technology_pfk, c_attribute_level_investment_options_size_pfk, c_attribute_level_investment_options_units_pfk, c_attribute_level_pk);
 \   ALTER TABLE ONLY public.tb_attribute_level DROP CONSTRAINT c_attribute_level_attribute_pfk;
       public         sozio_e2s_admin_role    false    206    206    206    206    206            n           2606    240192    tb_attributes c_attribute_pk 
   CONSTRAINT     g   ALTER TABLE ONLY public.tb_attributes
    ADD CONSTRAINT c_attribute_pk PRIMARY KEY (c_attributes_pk);
 F   ALTER TABLE ONLY public.tb_attributes DROP CONSTRAINT c_attribute_pk;
       public         sozio_e2s_admin_role    false    208            l           2606    240194 /   tb_attribute_scenarios c_attribute_scenarios_pk 
   CONSTRAINT     �  ALTER TABLE ONLY public.tb_attribute_scenarios
    ADD CONSTRAINT c_attribute_scenarios_pk PRIMARY KEY (c_attribute_development_scenario_pk, c_attribute_development_attributes_pfk, c_attribute_scenarios_technology_pfk, c_attribute_development_investment_option_size_pfk, c_attribute_development_investment_options_units_pfk, c_attribute_scenario_sub_technology_pfk, c_attribute_scenario_year_pk);
 Y   ALTER TABLE ONLY public.tb_attribute_scenarios DROP CONSTRAINT c_attribute_scenarios_pk;
       public         sozio_e2s_admin_role    false    207    207    207    207    207    207    207            p           2606    240196 )   tb_car_class_shares c_car_class_shares_pk 
   CONSTRAINT       ALTER TABLE ONLY public.tb_car_class_shares
    ADD CONSTRAINT c_car_class_shares_pk PRIMARY KEY (c_car_class_shares_technology_pfk, c_car_class_shares_investment_options_size_pk, c_car_class_shares_investment_options_units_pfk, c_car_class_shares_validity_year);
 S   ALTER TABLE ONLY public.tb_car_class_shares DROP CONSTRAINT c_car_class_shares_pk;
       public         postgres    false    209    209    209    209            t           2606    240198 +   tb_car_target_system c_car_target_system_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_car_target_system
    ADD CONSTRAINT c_car_target_system_pk PRIMARY KEY (c_car_target_system_sub_technology_pfk, c_car_target_year_pk, c_car_target_scenario_pk);
 U   ALTER TABLE ONLY public.tb_car_target_system DROP CONSTRAINT c_car_target_system_pk;
       public         postgres    false    211    211    211            x           2606    240200 '   tb_consumer_prices c_consumer_prices_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_consumer_prices
    ADD CONSTRAINT c_consumer_prices_pk PRIMARY KEY (c_consumertype_pfk, c_consumption_good_pfk, c_consumption_prices_scenario, c_consumption_prices_validity_time);
 Q   ALTER TABLE ONLY public.tb_consumer_prices DROP CONSTRAINT c_consumer_prices_pk;
       public         sozio_e2s_admin_role    false    213    213    213    213            z           2606    240202 !   tb_consumertype c_consumertype_pk 
   CONSTRAINT     n   ALTER TABLE ONLY public.tb_consumertype
    ADD CONSTRAINT c_consumertype_pk PRIMARY KEY (c_consumertype_pk);
 K   ALTER TABLE ONLY public.tb_consumertype DROP CONSTRAINT c_consumertype_pk;
       public         sozio_e2s_admin_role    false    214            |           2606    240204 )   tb_consumption_good c_consumption_good_pk 
   CONSTRAINT     z   ALTER TABLE ONLY public.tb_consumption_good
    ADD CONSTRAINT c_consumption_good_pk PRIMARY KEY (c_consumption_good_pk);
 S   ALTER TABLE ONLY public.tb_consumption_good DROP CONSTRAINT c_consumption_good_pk;
       public         sozio_e2s_admin_role    false    215            �           2606    240206 -   tb_economic_parameter c_economic_parameter_pk 
   CONSTRAINT       ALTER TABLE ONLY public.tb_economic_parameter
    ADD CONSTRAINT c_economic_parameter_pk PRIMARY KEY (c_technology_pfk, c_investment_options_units_pfk, c_regions_pfk, c_economic_parameter_validity_time, c_economic_parameter_types_pfk, c_economic_parameter_scenario_pk);
 W   ALTER TABLE ONLY public.tb_economic_parameter DROP CONSTRAINT c_economic_parameter_pk;
       public         sozio_e2s_admin_role    false    218    218    218    218    218    218            �           2606    240208 7   tb_economic_parameter_type c_economic_parameter_type_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_economic_parameter_type
    ADD CONSTRAINT c_economic_parameter_type_pk PRIMARY KEY (c_economic_parameter_types_pk);
 a   ALTER TABLE ONLY public.tb_economic_parameter_type DROP CONSTRAINT c_economic_parameter_type_pk;
       public         sozio_e2s_admin_role    false    219            �           2606    240210 /   tb_financial_parameter c_financial_parameter_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_financial_parameter
    ADD CONSTRAINT c_financial_parameter_pk PRIMARY KEY (c_investors_pfk, c_technology_pfk, c_investment_options_size_pk, c_investment_options_units_pfk, c_financial_parameter_scenario_pk);
 Y   ALTER TABLE ONLY public.tb_financial_parameter DROP CONSTRAINT c_financial_parameter_pk;
       public         sozio_e2s_admin_role    false    220    220    220    220    220            �           2606    240212 ;   tb_financial_parameter_types c_financial_parameter_types_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_financial_parameter_types
    ADD CONSTRAINT c_financial_parameter_types_pk PRIMARY KEY (c_financial_parameter_types_pk);
 e   ALTER TABLE ONLY public.tb_financial_parameter_types DROP CONSTRAINT c_financial_parameter_types_pk;
       public         sozio_e2s_admin_role    false    221            �           2606    240214    tb_fuels c_fuels_pk 
   CONSTRAINT     Y   ALTER TABLE ONLY public.tb_fuels
    ADD CONSTRAINT c_fuels_pk PRIMARY KEY (c_fuels_pk);
 =   ALTER TABLE ONLY public.tb_fuels DROP CONSTRAINT c_fuels_pk;
       public         sozio_e2s_admin_role    false    222            �           2606    240216    tb_grid_level c_grid_level_pk 
   CONSTRAINT     h   ALTER TABLE ONLY public.tb_grid_level
    ADD CONSTRAINT c_grid_level_pk PRIMARY KEY (c_grid_level_pk);
 G   ALTER TABLE ONLY public.tb_grid_level DROP CONSTRAINT c_grid_level_pk;
       public         sozio_e2s_admin_role    false    223            �           2606    240218 *   tb_importances c_importance_attribute_pfk_ 
   CONSTRAINT       ALTER TABLE ONLY public.tb_importances
    ADD CONSTRAINT c_importance_attribute_pfk_ PRIMARY KEY (c_importance_attribute_pfk, c_importances_technology_pfk, c_importances_investment_options_size_pfk, c_importances_investment_options_units_pfk, c_importance_respondend_pfk);
 T   ALTER TABLE ONLY public.tb_importances DROP CONSTRAINT c_importance_attribute_pfk_;
       public         sozio_e2s_admin_role    false    224    224    224    224    224            �           2606    240220 -   tb_investment_options c_investment_options_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_investment_options
    ADD CONSTRAINT c_investment_options_pk PRIMARY KEY (c_technology_pfk, c_investment_options_size_pk, c_investment_options_units_pfk);
 W   ALTER TABLE ONLY public.tb_investment_options DROP CONSTRAINT c_investment_options_pk;
       public         sozio_e2s_admin_role    false    225    225    225            �           2606    240222 1   tb_investor_stock_share c_investor_stock_share_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_investor_stock_share
    ADD CONSTRAINT c_investor_stock_share_pk PRIMARY KEY (c_investor_stock_share_technology_pk, c_investor_stock_share_investors_pk, c_investor_stock_share_validity_year_pk);
 [   ALTER TABLE ONLY public.tb_investor_stock_share DROP CONSTRAINT c_investor_stock_share_pk;
       public         postgres    false    226    226    226            �           2606    240224    tb_investors c_investors_pk 
   CONSTRAINT     e   ALTER TABLE ONLY public.tb_investors
    ADD CONSTRAINT c_investors_pk PRIMARY KEY (c_investors_pk);
 E   ALTER TABLE ONLY public.tb_investors DROP CONSTRAINT c_investors_pk;
       public         sozio_e2s_admin_role    false    227            b           2606    240226 2   mapping_profile_region c_mapping_profile_region_pk 
   CONSTRAINT       ALTER TABLE ONLY public.mapping_profile_region
    ADD CONSTRAINT c_mapping_profile_region_pk PRIMARY KEY (c_map_profile_reg_profile_pfk, c_map_profile_reg_scenario_pfk, c_map_profile_reg_reference_year_pfk, c_map_profile_reg_profile_type_pfk, c_map_profile_reg_regions_pfk);
 \   ALTER TABLE ONLY public.mapping_profile_region DROP CONSTRAINT c_mapping_profile_region_pk;
       public         postgres    false    202    202    202    202    202            �           2606    240228 !   tb_market_phase c_market_phase_pk 
   CONSTRAINT     n   ALTER TABLE ONLY public.tb_market_phase
    ADD CONSTRAINT c_market_phase_pk PRIMARY KEY (c_market_phase_pk);
 K   ALTER TABLE ONLY public.tb_market_phase DROP CONSTRAINT c_market_phase_pk;
       public         sozio_e2s_admin_role    false    228            �           2606    240232 :   tb_political_instrument_types c_political_instrument_types 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_political_instrument_types
    ADD CONSTRAINT c_political_instrument_types PRIMARY KEY (c_political_instrument_type_pk);
 d   ALTER TABLE ONLY public.tb_political_instrument_types DROP CONSTRAINT c_political_instrument_types;
       public         sozio_e2s_admin_role    false    230            �           2606    240236 -   tb_power_plant_status c_power_plant_status_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_power_plant_status
    ADD CONSTRAINT c_power_plant_status_pk PRIMARY KEY (c_power_plant_status_pk);
 W   ALTER TABLE ONLY public.tb_power_plant_status DROP CONSTRAINT c_power_plant_status_pk;
       public         sozio_e2s_admin_role    false    232            �           2606    240240 7   tb_profile_characteristics c_profile_characteristics_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_profile_characteristics
    ADD CONSTRAINT c_profile_characteristics_pk PRIMARY KEY (c_profile_pk, c_profile_scenario_pk, c_profile_reference_year_pk, c_profile_characteristrics_type_pfk);
 a   ALTER TABLE ONLY public.tb_profile_characteristics DROP CONSTRAINT c_profile_characteristics_pk;
       public         postgres    false    233    233    233    233            �           2606    240242    tb_profiles c_profiles_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_profiles
    ADD CONSTRAINT c_profiles_pk PRIMARY KEY (c_profiles_profile_pfk, c_profiles_profile_scenario_pfk, c_profiles_profile_reference_year_pfk, c_profiles_profile_characteristrics_type_pfk, c_profiles_timestamp_pk);
 C   ALTER TABLE ONLY public.tb_profiles DROP CONSTRAINT c_profiles_pk;
       public         postgres    false    235    235    235    235    235            `           2606    240246    tb_regions c_reginos_pk 
   CONSTRAINT     _   ALTER TABLE ONLY public.tb_regions
    ADD CONSTRAINT c_reginos_pk PRIMARY KEY (c_regions_pk);
 A   ALTER TABLE ONLY public.tb_regions DROP CONSTRAINT c_reginos_pk;
       public         sozio_e2s_admin_role    false    201            �           2606    240248 %   tb_regional_level c_regional_level_pk 
   CONSTRAINT     t   ALTER TABLE ONLY public.tb_regional_level
    ADD CONSTRAINT c_regional_level_pk PRIMARY KEY (c_regional_level_pk);
 O   ALTER TABLE ONLY public.tb_regional_level DROP CONSTRAINT c_regional_level_pk;
       public         sozio_e2s_admin_role    false    236            �           2606    240250 ?   tb_relation_fuels_technologies c_relation_fuels_technologies_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_fuels_technologies
    ADD CONSTRAINT c_relation_fuels_technologies_pk PRIMARY KEY (c_technology_pfk, c_fuels_pfk);
 i   ALTER TABLE ONLY public.tb_relation_fuels_technologies DROP CONSTRAINT c_relation_fuels_technologies_pk;
       public         sozio_e2s_admin_role    false    237    237            �           2606    240252 W   tb_relation_investment_option_alternatives c_relation_investment_option_alternatives_pk 
   CONSTRAINT     C  ALTER TABLE ONLY public.tb_relation_investment_option_alternatives
    ADD CONSTRAINT c_relation_investment_option_alternatives_pk PRIMARY KEY (c_rel_inv_op_altern_technology_pfk, c_rel_inv_op_altern_investment_option_size_pfk, c_rel_inv_op_altern_investment_option_size_units_pfk, c_rel_inv_op_altern_sub_technology_pfk);
 �   ALTER TABLE ONLY public.tb_relation_investment_option_alternatives DROP CONSTRAINT c_relation_investment_option_alternatives_pk;
       public         sozio_e2s_admin_role    false    238    238    238    238            �           2606    240254 C   tb_relation_regional_level_stock c_relation_regional_level_stock_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_regional_level_stock
    ADD CONSTRAINT c_relation_regional_level_stock_pk PRIMARY KEY (c_regional_coverage_pfk, c_regional_level_pfk, c_stock_scenario_pfk);
 m   ALTER TABLE ONLY public.tb_relation_regional_level_stock DROP CONSTRAINT c_relation_regional_level_stock_pk;
       public         sozio_e2s_admin_role    false    242    242    242            �           2606    240256 )   tb_relation_regions c_relation_regions_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_regions
    ADD CONSTRAINT c_relation_regions_pk PRIMARY KEY (c_regions_main_pfk, c_regions_sub_pfk);
 S   ALTER TABLE ONLY public.tb_relation_regions DROP CONSTRAINT c_relation_regions_pk;
       public         sozio_e2s_admin_role    false    243    243            �           2606    240258    tb_respondends c_respondend_pk 
   CONSTRAINT     i   ALTER TABLE ONLY public.tb_respondends
    ADD CONSTRAINT c_respondend_pk PRIMARY KEY (c_respondend_pk);
 H   ALTER TABLE ONLY public.tb_respondends DROP CONSTRAINT c_respondend_pk;
       public         sozio_e2s_admin_role    false    245            �           2606    240261 5   tb_respondends_sub_groups c_respondends_sub_groups_pk 
   CONSTRAINT       ALTER TABLE ONLY public.tb_respondends_sub_groups
    ADD CONSTRAINT c_respondends_sub_groups_pk PRIMARY KEY (c_respondends_sub_groups_main_group_pk, c_respondends_sub_groups_sub_group_pk, c_respondends_sub_groups_respondend_pfk, c_respondends_sub_groups_technology_pfk);
 _   ALTER TABLE ONLY public.tb_respondends_sub_groups DROP CONSTRAINT c_respondends_sub_groups_pk;
       public         postgres    false    246    246    246    246            �           2606    240263    tb_sources c_sources_pk 
   CONSTRAINT     _   ALTER TABLE ONLY public.tb_sources
    ADD CONSTRAINT c_sources_pk PRIMARY KEY (c_sources_pk);
 A   ALTER TABLE ONLY public.tb_sources DROP CONSTRAINT c_sources_pk;
       public         sozio_e2s_admin_role    false    247            �           2606    240265 2   tb_specific_consumption c_specific_consumptione_pk 
   CONSTRAINT     e  ALTER TABLE ONLY public.tb_specific_consumption
    ADD CONSTRAINT c_specific_consumptione_pk PRIMARY KEY (c_specific_consumption_year, c_specific_consumption_technology_pfk, c_specific_consumption_sub_technology_pfk, c_specific_consumption_investment_options_size_pfk, c_specific_consumption_investment_options_units_pfk, c_specific_consumption_scenario);
 \   ALTER TABLE ONLY public.tb_specific_consumption DROP CONSTRAINT c_specific_consumptione_pk;
       public         postgres    false    248    248    248    248    248    248            �           2606    240267 3   tb_specific_emissions_cv c_specific_emissions_cv_pk 
   CONSTRAINT     C  ALTER TABLE ONLY public.tb_specific_emissions_cv
    ADD CONSTRAINT c_specific_emissions_cv_pk PRIMARY KEY (c_specific_emissions_construction_year_pk, c_specific_emissions_technology_pfk, c_specific_emissions_investment_options_size_pk, c_specific_emissions_investment_options_units_pfk, c_specific_emissions_scenario_pk);
 ]   ALTER TABLE ONLY public.tb_specific_emissions_cv DROP CONSTRAINT c_specific_emissions_cv_pk;
       public         postgres    false    249    249    249    249    249            �           2606    240269 M   tb_specific_emissions_electricity_mix c_specific_emissions_electricity_mix_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_specific_emissions_electricity_mix
    ADD CONSTRAINT c_specific_emissions_electricity_mix_pk PRIMARY KEY (c_specific_emissions_electricity_mix_year, c_specific_emissions_electricity_mix_scenario);
 w   ALTER TABLE ONLY public.tb_specific_emissions_electricity_mix DROP CONSTRAINT c_specific_emissions_electricity_mix_pk;
       public         postgres    false    250    250            �           2606    240271 (   tb_stock_parameter c_stock_parametere_pk 
   CONSTRAINT     x   ALTER TABLE ONLY public.tb_stock_parameter
    ADD CONSTRAINT c_stock_parametere_pk PRIMARY KEY (c_stock_parameter_pk);
 R   ALTER TABLE ONLY public.tb_stock_parameter DROP CONSTRAINT c_stock_parametere_pk;
       public         sozio_e2s_admin_role    false    252            �           2606    240273    tb_stock_pv c_stock_pv_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_pv
    ADD CONSTRAINT c_stock_pv_pk PRIMARY KEY (c_stock_pv_technology_pfk, c_stock_pv_id_pk, c_stock_pv_regions_nuts3_pfk);
 C   ALTER TABLE ONLY public.tb_stock_pv DROP CONSTRAINT c_stock_pv_pk;
       public         sozio_e2s_admin_role    false    253    253    253            �           2606    240275 %   tb_stock_scenario c_stock_scenario_pk 
   CONSTRAINT     u   ALTER TABLE ONLY public.tb_stock_scenario
    ADD CONSTRAINT c_stock_scenario_pk PRIMARY KEY (tb_stock_scenario_pk);
 O   ALTER TABLE ONLY public.tb_stock_scenario DROP CONSTRAINT c_stock_scenario_pk;
       public         sozio_e2s_admin_role    false    254            r           2606    240277 6   tb_car_stock_scenario c_stock_scenario_technology_pfk_ 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_car_stock_scenario
    ADD CONSTRAINT c_stock_scenario_technology_pfk_ PRIMARY KEY (c_stock_scenario_validity_time_pk, c_stock_scenario_scenario_pk, c_stock_scenario_technology_pfk);
 `   ALTER TABLE ONLY public.tb_car_stock_scenario DROP CONSTRAINT c_stock_scenario_technology_pfk_;
       public         postgres    false    210    210    210            �           2606    240279 3   tb_sub_technology_shares c_sub_technology_shares_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_sub_technology_shares
    ADD CONSTRAINT c_sub_technology_shares_pk PRIMARY KEY (c_sub_tec_shares_technology_pfk, c_sub_tec_shares_validity_year);
 ]   ALTER TABLE ONLY public.tb_sub_technology_shares DROP CONSTRAINT c_sub_technology_shares_pk;
       public         postgres    false    255    255            �           2606    240281 .   tb_potlitical_target c_tb_potlitical_target_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_potlitical_target
    ADD CONSTRAINT c_tb_potlitical_target_pk PRIMARY KEY (c_regions_pfk, c_technology_pfk, c_investment_options_size_pk, c_investment_options_units_pfk);
 X   ALTER TABLE ONLY public.tb_potlitical_target DROP CONSTRAINT c_tb_potlitical_target_pk;
       public         sozio_e2s_admin_role    false    231    231    231    231            �           2606    240283 G   tb_technical_characteristics_types c_technical_characteristics_types_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_technical_characteristics_types
    ADD CONSTRAINT c_technical_characteristics_types_pk PRIMARY KEY (c_technical_characteristics_types_pk);
 q   ALTER TABLE ONLY public.tb_technical_characteristics_types DROP CONSTRAINT c_technical_characteristics_types_pk;
       public         sozio_e2s_admin_role    false    256            �           2606    240289 !   tb_technologies c_technologies_pk 
   CONSTRAINT     l   ALTER TABLE ONLY public.tb_technologies
    ADD CONSTRAINT c_technologies_pk PRIMARY KEY (c_technology_pk);
 K   ALTER TABLE ONLY public.tb_technologies DROP CONSTRAINT c_technologies_pk;
       public         sozio_e2s_admin_role    false    257            v           2606    240291    tb_cars_stock c_technology_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_cars_stock
    ADD CONSTRAINT c_technology_pk PRIMARY KEY (c_technology_pk, c_registration_year, c_stock_year);
 G   ALTER TABLE ONLY public.tb_cars_stock DROP CONSTRAINT c_technology_pk;
       public         sozio_e2s_admin_user    false    212    212    212            �           2606    240293    tb_units c_units_pk 
   CONSTRAINT     Y   ALTER TABLE ONLY public.tb_units
    ADD CONSTRAINT c_units_pk PRIMARY KEY (c_units_pk);
 =   ALTER TABLE ONLY public.tb_units DROP CONSTRAINT c_units_pk;
       public         sozio_e2s_admin_role    false    259            �           2606    240295 '   tb_utilities c_utilities_attribute_pfk_ 
   CONSTRAINT     >  ALTER TABLE ONLY public.tb_utilities
    ADD CONSTRAINT c_utilities_attribute_pfk_ PRIMARY KEY (c_utilities_attribute_pfk, c_utilities_technology_pfk, c_utilities_investment_options_size_pfk, c_utilities_investment_options_units_pfk, c_utilities_attribute_level_pfk, c_utilities_respondend_pfk, c_utilities_level_pk);
 Q   ALTER TABLE ONLY public.tb_utilities DROP CONSTRAINT c_utilities_attribute_pfk_;
       public         sozio_e2s_admin_role    false    260    260    260    260    260    260    260            h           2606    240298 L   tb_application_characteristics_types tb_application_characteristics_types_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_application_characteristics_types
    ADD CONSTRAINT tb_application_characteristics_types_pk PRIMARY KEY (c_application_characteristic_types_pk);
 v   ALTER TABLE ONLY public.tb_application_characteristics_types DROP CONSTRAINT tb_application_characteristics_types_pk;
       public         sozio_e2s_admin_role    false    205            ~           2606    240300 :   tb_economic_basic_parameter tb_economic_basic_parameter_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_economic_basic_parameter
    ADD CONSTRAINT tb_economic_basic_parameter_pk PRIMARY KEY (c_economic_basic_parameter_type_pk, c_economic_basic_parameter_validity_time, c_economic_basic_parameter_scenario);
 d   ALTER TABLE ONLY public.tb_economic_basic_parameter DROP CONSTRAINT tb_economic_basic_parameter_pk;
       public         sozio_e2s_admin_role    false    216    216    216            �           2606    240302 4   tb_economic_basics_types tb_economic_basics_types_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_economic_basics_types
    ADD CONSTRAINT tb_economic_basics_types_pk PRIMARY KEY (c_economic_basics_types_pk);
 ^   ALTER TABLE ONLY public.tb_economic_basics_types DROP CONSTRAINT tb_economic_basics_types_pk;
       public         sozio_e2s_admin_role    false    217            �           2606    240306 4   tb_political_incentives tb_political_incentives_pkey 
   CONSTRAINT     i  ALTER TABLE ONLY public.tb_political_incentives
    ADD CONSTRAINT tb_political_incentives_pkey PRIMARY KEY (c_technology_pfk, c_investment_options_size_pfk, c_investment_options_units_pfk, c_political_incentive_validity_time, c_political_instrument_scenario, c_political_incentive_application_fk, c_political_incentive_region, c_political_instrument_type_fk);
 ^   ALTER TABLE ONLY public.tb_political_incentives DROP CONSTRAINT tb_political_incentives_pkey;
       public         sozio_e2s_admin_role    false    229    229    229    229    229    229    229    229            �           2606    240310 $   tb_profile_types tb_profile_types_pk 
   CONSTRAINT     q   ALTER TABLE ONLY public.tb_profile_types
    ADD CONSTRAINT tb_profile_types_pk PRIMARY KEY (c_profile_type_pk);
 N   ALTER TABLE ONLY public.tb_profile_types DROP CONSTRAINT tb_profile_types_pk;
       public         postgres    false    234            �           2606    240312 V   tb_relation_investment_option_application tb_relation_investment_option_application_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_investment_option_application
    ADD CONSTRAINT tb_relation_investment_option_application_pk PRIMARY KEY (c_application_pfk, c_technology_pfk, c_investment_options_size_pk, c_investment_options_units_pfk);
 �   ALTER TABLE ONLY public.tb_relation_investment_option_application DROP CONSTRAINT tb_relation_investment_option_application_pk;
       public         sozio_e2s_admin_role    false    239    239    239    239            �           2606    240314 P   tb_relation_investor_investment_option tb_relation_investor_investment_option_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_investor_investment_option
    ADD CONSTRAINT tb_relation_investor_investment_option_pk PRIMARY KEY (c_technology_pfk, c_investment_options_size_pfk, c_investment_options_units_pfk, c_investors_pfk);
 z   ALTER TABLE ONLY public.tb_relation_investor_investment_option DROP CONSTRAINT tb_relation_investor_investment_option_pk;
       public         sozio_e2s_admin_role    false    241    241    241    241            �           2606    240316 ,   tb_relation_investor tb_relation_investor_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_investor
    ADD CONSTRAINT tb_relation_investor_pk PRIMARY KEY (c_relation_investor_main_pfk, c_relation_investor_sub_pfk);
 V   ALTER TABLE ONLY public.tb_relation_investor DROP CONSTRAINT tb_relation_investor_pk;
       public         sozio_e2s_admin_role    false    240    240            �           2606    240318 4   tb_relation_technologies tb_relation_technologies_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_technologies
    ADD CONSTRAINT tb_relation_technologies_pk PRIMARY KEY (c_technology_main_pfk, c_technology_sub_pfk);
 ^   ALTER TABLE ONLY public.tb_relation_technologies DROP CONSTRAINT tb_relation_technologies_pk;
       public         sozio_e2s_admin_role    false    244    244            �           2606    240320    tb_stock_bat tb_stock_bat_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_bat
    ADD CONSTRAINT tb_stock_bat_pk PRIMARY KEY (c_stock_bat_technology_pfk, c_stock_bat_regions_pfk, c_stock_bat_initial_operation_pk, c_stock_bat_scenario_pk);
 F   ALTER TABLE ONLY public.tb_stock_bat DROP CONSTRAINT tb_stock_bat_pk;
       public         postgres    false    251    251    251    251            �           2606    240322 >   tb_technology_characteristics tb_technology_characteristics_pk 
   CONSTRAINT     �   ALTER TABLE ONLY public.tb_technology_characteristics
    ADD CONSTRAINT tb_technology_characteristics_pk PRIMARY KEY (c_technology_pfk, c_technology_characteristics_types_pfk, c_technology_characteristics_validity_period_pk);
 h   ALTER TABLE ONLY public.tb_technology_characteristics DROP CONSTRAINT tb_technology_characteristics_pk;
       public         sozio_e2s_admin_role    false    258    258    258            �           826    241040     DEFAULT PRIVILEGES FOR SEQUENCES    DEFAULT ACL     �   ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public REVOKE ALL ON SEQUENCES  FROM postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON SEQUENCES  TO sozio_e2s_admin_role;
            public       postgres    false                       2606    240325 S   tb_profile_characteristics c_profile_types_tb_generation_profile_characteristics_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_profile_characteristics
    ADD CONSTRAINT c_profile_types_tb_generation_profile_characteristics_fk FOREIGN KEY (c_profile_characteristrics_type_pfk) REFERENCES public.tb_profile_types(c_profile_type_pk) ON UPDATE CASCADE;
 }   ALTER TABLE ONLY public.tb_profile_characteristics DROP CONSTRAINT c_profile_types_tb_generation_profile_characteristics_fk;
       public       postgres    false    3746    234    233            �           2606    240330 $   tb_regions fk_regional_level_regions    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_regions
    ADD CONSTRAINT fk_regional_level_regions FOREIGN KEY (c_regions_level) REFERENCES public.tb_regional_level(c_regional_level_pk) ON UPDATE CASCADE;
 N   ALTER TABLE ONLY public.tb_regions DROP CONSTRAINT fk_regional_level_regions;
       public       sozio_e2s_admin_role    false    3750    236    201            �           826    241041    DEFAULT PRIVILEGES FOR TABLES    DEFAULT ACL     �   ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public REVOKE ALL ON TABLES  FROM postgres;
ALTER DEFAULT PRIVILEGES FOR ROLE postgres IN SCHEMA public GRANT ALL ON TABLES  TO sozio_e2s_admin_role;
            public       postgres    false            �           2606    240335    tb_regions sources_regions_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_regions
    ADD CONSTRAINT sources_regions_fk FOREIGN KEY (c_regions_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 G   ALTER TABLE ONLY public.tb_regions DROP CONSTRAINT sources_regions_fk;
       public       sozio_e2s_admin_role    false    3772    247    201            �           2606    240340 ^   tb_application_characteristics tb_application_characteristics_types_tb_application_characteris    FK CONSTRAINT     /  ALTER TABLE ONLY public.tb_application_characteristics
    ADD CONSTRAINT tb_application_characteristics_types_tb_application_characteris FOREIGN KEY (c_application_characteristic_types_pk) REFERENCES public.tb_application_characteristics_types(c_application_characteristic_types_pk) ON UPDATE CASCADE;
 �   ALTER TABLE ONLY public.tb_application_characteristics DROP CONSTRAINT tb_application_characteristics_types_tb_application_characteris;
       public       sozio_e2s_admin_role    false    3688    205    204            �           2606    240345 O   tb_application_characteristics tb_application_tb_application_characteristics_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_application_characteristics
    ADD CONSTRAINT tb_application_tb_application_characteristics_fk FOREIGN KEY (c_application_pfk) REFERENCES public.tb_application(c_application_pk) ON UPDATE CASCADE;
 y   ALTER TABLE ONLY public.tb_application_characteristics DROP CONSTRAINT tb_application_tb_application_characteristics_fk;
       public       sozio_e2s_admin_role    false    3684    203    204                       2606    240350 ;   tb_political_incentives tb_application_tb_feed_in_tariff_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_political_incentives
    ADD CONSTRAINT tb_application_tb_feed_in_tariff_fk FOREIGN KEY (c_political_incentive_application_fk) REFERENCES public.tb_application(c_application_pk) ON UPDATE CASCADE;
 e   ALTER TABLE ONLY public.tb_political_incentives DROP CONSTRAINT tb_application_tb_feed_in_tariff_fk;
       public       sozio_e2s_admin_role    false    3684    203    229                       2606    240355 e   tb_relation_investment_option_application tb_application_tb_relation_investment_option_application_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_investment_option_application
    ADD CONSTRAINT tb_application_tb_relation_investment_option_application_fk FOREIGN KEY (c_application_pfk) REFERENCES public.tb_application(c_application_pk) ON UPDATE CASCADE;
 �   ALTER TABLE ONLY public.tb_relation_investment_option_application DROP CONSTRAINT tb_application_tb_relation_investment_option_application_fk;
       public       sozio_e2s_admin_role    false    3684    203    239            7           2606    240371 #   tb_stock_pv tb_application_tb_stock    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_pv
    ADD CONSTRAINT tb_application_tb_stock FOREIGN KEY (c_stock_pv_application_fk) REFERENCES public.tb_application(c_application_pk) MATCH FULL;
 M   ALTER TABLE ONLY public.tb_stock_pv DROP CONSTRAINT tb_application_tb_stock;
       public       sozio_e2s_admin_role    false    3684    203    253            H           2606    240376 /   tb_utilities tb_attribute_level_tb_utilities_fk    FK CONSTRAINT       ALTER TABLE ONLY public.tb_utilities
    ADD CONSTRAINT tb_attribute_level_tb_utilities_fk FOREIGN KEY (c_utilities_investment_options_size_pfk, c_utilities_investment_options_units_pfk, c_utilities_attribute_pfk, c_utilities_technology_pfk, c_utilities_attribute_level_pfk) REFERENCES public.tb_attribute_level(c_attribute_level_investment_options_size_pfk, c_attribute_level_investment_options_units_pfk, c_attribute_level_attribute_pfk, c_attribute_level_technology_pfk, c_attribute_level_pk) ON UPDATE CASCADE;
 Y   ALTER TABLE ONLY public.tb_utilities DROP CONSTRAINT tb_attribute_level_tb_utilities_fk;
       public       sozio_e2s_admin_role    false    3690    206    206    206    206    206    260    260    260    260    260            �           2606    240381 C   tb_attribute_level tb_attributes_c_attribute_level_attribute_pfk_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_attribute_level
    ADD CONSTRAINT tb_attributes_c_attribute_level_attribute_pfk_fk FOREIGN KEY (c_attribute_level_attribute_pfk) REFERENCES public.tb_attributes(c_attributes_pk) ON UPDATE CASCADE;
 m   ALTER TABLE ONLY public.tb_attribute_level DROP CONSTRAINT tb_attributes_c_attribute_level_attribute_pfk_fk;
       public       sozio_e2s_admin_role    false    3694    208    206            �           2606    240386 5   tb_attribute_scenarios tb_attributes_tb_attribute_454    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_attribute_scenarios
    ADD CONSTRAINT tb_attributes_tb_attribute_454 FOREIGN KEY (c_attribute_development_attributes_pfk) REFERENCES public.tb_attributes(c_attributes_pk);
 _   ALTER TABLE ONLY public.tb_attribute_scenarios DROP CONSTRAINT tb_attributes_tb_attribute_454;
       public       sozio_e2s_admin_role    false    3694    208    207                       2606    240391 .   tb_importances tb_attributes_tb_importances_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_importances
    ADD CONSTRAINT tb_attributes_tb_importances_fk FOREIGN KEY (c_importance_attribute_pfk) REFERENCES public.tb_attributes(c_attributes_pk) ON UPDATE CASCADE;
 X   ALTER TABLE ONLY public.tb_importances DROP CONSTRAINT tb_attributes_tb_importances_fk;
       public       sozio_e2s_admin_role    false    3694    208    224            �           2606    240396 [   tb_economic_basic_parameter tb_basic_economic_parameter_types_tb_basic_economic_parameter_f    FK CONSTRAINT       ALTER TABLE ONLY public.tb_economic_basic_parameter
    ADD CONSTRAINT tb_basic_economic_parameter_types_tb_basic_economic_parameter_f FOREIGN KEY (c_economic_basic_parameter_type_pk) REFERENCES public.tb_economic_basics_types(c_economic_basics_types_pk) ON UPDATE CASCADE;
 �   ALTER TABLE ONLY public.tb_economic_basic_parameter DROP CONSTRAINT tb_basic_economic_parameter_types_tb_basic_economic_parameter_f;
       public       sozio_e2s_admin_role    false    3712    217    216            �           2606    240401 C   tb_consumer_prices tb_consumertype_tb_consumer_price_development_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_consumer_prices
    ADD CONSTRAINT tb_consumertype_tb_consumer_price_development_fk FOREIGN KEY (c_consumertype_pfk) REFERENCES public.tb_consumertype(c_consumertype_pk) ON UPDATE CASCADE;
 m   ALTER TABLE ONLY public.tb_consumer_prices DROP CONSTRAINT tb_consumertype_tb_consumer_price_development_fk;
       public       sozio_e2s_admin_role    false    3706    214    213            �           2606    240406 G   tb_consumer_prices tb_consumption_good_tb_consumer_price_development_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_consumer_prices
    ADD CONSTRAINT tb_consumption_good_tb_consumer_price_development_fk FOREIGN KEY (c_consumption_good_pfk) REFERENCES public.tb_consumption_good(c_consumption_good_pk) ON UPDATE CASCADE;
 q   ALTER TABLE ONLY public.tb_consumer_prices DROP CONSTRAINT tb_consumption_good_tb_consumer_price_development_fk;
       public       sozio_e2s_admin_role    false    3708    215    213            �           2606    240411 I   tb_economic_parameter tb_economic_parameter_type_tb_economic_parameter_fk    FK CONSTRAINT       ALTER TABLE ONLY public.tb_economic_parameter
    ADD CONSTRAINT tb_economic_parameter_type_tb_economic_parameter_fk FOREIGN KEY (c_economic_parameter_types_pfk) REFERENCES public.tb_economic_parameter_type(c_economic_parameter_types_pk) ON UPDATE CASCADE;
 s   ALTER TABLE ONLY public.tb_economic_parameter DROP CONSTRAINT tb_economic_parameter_type_tb_economic_parameter_fk;
       public       sozio_e2s_admin_role    false    3716    219    218            �           2606    240416 M   tb_financial_parameter tb_financial_parameter_types_tb_financial_parameter_fk    FK CONSTRAINT       ALTER TABLE ONLY public.tb_financial_parameter
    ADD CONSTRAINT tb_financial_parameter_types_tb_financial_parameter_fk FOREIGN KEY (c_financial_parameter_types_pk) REFERENCES public.tb_financial_parameter_types(c_financial_parameter_types_pk) ON UPDATE CASCADE;
 w   ALTER TABLE ONLY public.tb_financial_parameter DROP CONSTRAINT tb_financial_parameter_types_tb_financial_parameter_fk;
       public       sozio_e2s_admin_role    false    3720    221    220                       2606    240421 F   tb_relation_fuels_technologies tb_fuels_tb_relation_fuel_technology_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_fuels_technologies
    ADD CONSTRAINT tb_fuels_tb_relation_fuel_technology_fk FOREIGN KEY (c_fuels_pfk) REFERENCES public.tb_fuels(c_fuels_pk) ON UPDATE CASCADE;
 p   ALTER TABLE ONLY public.tb_relation_fuels_technologies DROP CONSTRAINT tb_fuels_tb_relation_fuel_technology_fk;
       public       sozio_e2s_admin_role    false    3722    222    237            8           2606    240431 %   tb_stock_pv tb_grid_level_tb_stock_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_pv
    ADD CONSTRAINT tb_grid_level_tb_stock_fk FOREIGN KEY (c_stock_pv_grid_level_fk) REFERENCES public.tb_grid_level(c_grid_level_pk) ON UPDATE CASCADE;
 O   ALTER TABLE ONLY public.tb_stock_pv DROP CONSTRAINT tb_grid_level_tb_stock_fk;
       public       sozio_e2s_admin_role    false    3724    223    253            �           2606    240436 K   tb_attribute_level tb_investment_options_c_attribute_level_attribute_pfk_fk    FK CONSTRAINT     �  ALTER TABLE ONLY public.tb_attribute_level
    ADD CONSTRAINT tb_investment_options_c_attribute_level_attribute_pfk_fk FOREIGN KEY (c_attribute_level_investment_options_size_pfk, c_attribute_level_technology_pfk, c_attribute_level_investment_options_units_pfk) REFERENCES public.tb_investment_options(c_investment_options_size_pk, c_technology_pfk, c_investment_options_units_pfk) ON UPDATE CASCADE;
 u   ALTER TABLE ONLY public.tb_attribute_level DROP CONSTRAINT tb_investment_options_c_attribute_level_attribute_pfk_fk;
       public       sozio_e2s_admin_role    false    3728    225    225    225    206    206    206            �           2606    240441 5   tb_attribute_scenarios tb_investment_options_tb_at433    FK CONSTRAINT     w  ALTER TABLE ONLY public.tb_attribute_scenarios
    ADD CONSTRAINT tb_investment_options_tb_at433 FOREIGN KEY (c_attribute_development_investment_option_size_pfk, c_attribute_scenarios_technology_pfk, c_attribute_development_investment_options_units_pfk) REFERENCES public.tb_investment_options(c_investment_options_size_pk, c_technology_pfk, c_investment_options_units_pfk);
 _   ALTER TABLE ONLY public.tb_attribute_scenarios DROP CONSTRAINT tb_investment_options_tb_at433;
       public       sozio_e2s_admin_role    false    3728    225    225    225    207    207    207            �           2606    240446 @   tb_car_class_shares tb_investment_options_tb_car_class_shares_fk    FK CONSTRAINT     �  ALTER TABLE ONLY public.tb_car_class_shares
    ADD CONSTRAINT tb_investment_options_tb_car_class_shares_fk FOREIGN KEY (c_car_class_shares_investment_options_size_pk, c_car_class_shares_technology_pfk, c_car_class_shares_investment_options_units_pfk) REFERENCES public.tb_investment_options(c_investment_options_size_pk, c_technology_pfk, c_investment_options_units_pfk) ON UPDATE CASCADE;
 j   ALTER TABLE ONLY public.tb_car_class_shares DROP CONSTRAINT tb_investment_options_tb_car_class_shares_fk;
       public       postgres    false    3728    225    225    225    209    209    209            �           2606    240451 D   tb_economic_parameter tb_investment_options_tb_economic_parameter_fk    FK CONSTRAINT     X  ALTER TABLE ONLY public.tb_economic_parameter
    ADD CONSTRAINT tb_investment_options_tb_economic_parameter_fk FOREIGN KEY (c_technology_pfk, c_investment_options_size_pk, c_investment_options_units_pfk) REFERENCES public.tb_investment_options(c_technology_pfk, c_investment_options_size_pk, c_investment_options_units_pfk) ON UPDATE CASCADE;
 n   ALTER TABLE ONLY public.tb_economic_parameter DROP CONSTRAINT tb_investment_options_tb_economic_parameter_fk;
       public       sozio_e2s_admin_role    false    3728    225    225    225    218    218    218                       2606    240456 B   tb_political_incentives tb_investment_options_tb_feed_in_tariff_fk    FK CONSTRAINT     W  ALTER TABLE ONLY public.tb_political_incentives
    ADD CONSTRAINT tb_investment_options_tb_feed_in_tariff_fk FOREIGN KEY (c_technology_pfk, c_investment_options_size_pfk, c_investment_options_units_pfk) REFERENCES public.tb_investment_options(c_technology_pfk, c_investment_options_size_pk, c_investment_options_units_pfk) ON UPDATE CASCADE;
 l   ALTER TABLE ONLY public.tb_political_incentives DROP CONSTRAINT tb_investment_options_tb_feed_in_tariff_fk;
       public       sozio_e2s_admin_role    false    3728    225    225    225    229    229    229            �           2606    240461 F   tb_financial_parameter tb_investment_options_tb_financial_parameter_fk    FK CONSTRAINT     Z  ALTER TABLE ONLY public.tb_financial_parameter
    ADD CONSTRAINT tb_investment_options_tb_financial_parameter_fk FOREIGN KEY (c_technology_pfk, c_investment_options_size_pk, c_investment_options_units_pfk) REFERENCES public.tb_investment_options(c_technology_pfk, c_investment_options_size_pk, c_investment_options_units_pfk) ON UPDATE CASCADE;
 p   ALTER TABLE ONLY public.tb_financial_parameter DROP CONSTRAINT tb_investment_options_tb_financial_parameter_fk;
       public       sozio_e2s_admin_role    false    3728    225    225    225    220    220    220                       2606    240466 6   tb_importances tb_investment_options_tb_importances_fk    FK CONSTRAINT     o  ALTER TABLE ONLY public.tb_importances
    ADD CONSTRAINT tb_investment_options_tb_importances_fk FOREIGN KEY (c_importances_investment_options_size_pfk, c_importances_technology_pfk, c_importances_investment_options_units_pfk) REFERENCES public.tb_investment_options(c_investment_options_size_pk, c_technology_pfk, c_investment_options_units_pfk) ON UPDATE CASCADE;
 `   ALTER TABLE ONLY public.tb_importances DROP CONSTRAINT tb_investment_options_tb_importances_fk;
       public       sozio_e2s_admin_role    false    3728    225    225    225    224    224    224                       2606    240476 j   tb_relation_investment_option_alternatives tb_investment_options_tb_relation_investment_option_alternat978    FK CONSTRAINT     �  ALTER TABLE ONLY public.tb_relation_investment_option_alternatives
    ADD CONSTRAINT tb_investment_options_tb_relation_investment_option_alternat978 FOREIGN KEY (c_rel_inv_op_altern_investment_option_size_pfk, c_rel_inv_op_altern_technology_pfk, c_rel_inv_op_altern_investment_option_size_units_pfk) REFERENCES public.tb_investment_options(c_investment_options_size_pk, c_technology_pfk, c_investment_options_units_pfk) ON UPDATE CASCADE;
 �   ALTER TABLE ONLY public.tb_relation_investment_option_alternatives DROP CONSTRAINT tb_investment_options_tb_relation_investment_option_alternat978;
       public       sozio_e2s_admin_role    false    3728    225    225    225    238    238    238                       2606    240481 i   tb_relation_investment_option_application tb_investment_options_tb_relation_investment_option_application    FK CONSTRAINT     }  ALTER TABLE ONLY public.tb_relation_investment_option_application
    ADD CONSTRAINT tb_investment_options_tb_relation_investment_option_application FOREIGN KEY (c_investment_options_size_pk, c_technology_pfk, c_investment_options_units_pfk) REFERENCES public.tb_investment_options(c_investment_options_size_pk, c_technology_pfk, c_investment_options_units_pfk) ON UPDATE CASCADE;
 �   ALTER TABLE ONLY public.tb_relation_investment_option_application DROP CONSTRAINT tb_investment_options_tb_relation_investment_option_application;
       public       sozio_e2s_admin_role    false    3728    225    225    225    239    239    239            "           2606    240486 f   tb_relation_investor_investment_option tb_investment_options_tb_relation_investor_investment_option_fk    FK CONSTRAINT     {  ALTER TABLE ONLY public.tb_relation_investor_investment_option
    ADD CONSTRAINT tb_investment_options_tb_relation_investor_investment_option_fk FOREIGN KEY (c_technology_pfk, c_investment_options_size_pfk, c_investment_options_units_pfk) REFERENCES public.tb_investment_options(c_technology_pfk, c_investment_options_size_pk, c_investment_options_units_pfk) ON UPDATE CASCADE;
 �   ALTER TABLE ONLY public.tb_relation_investor_investment_option DROP CONSTRAINT tb_investment_options_tb_relation_investor_investment_option_fk;
       public       sozio_e2s_admin_role    false    3728    225    225    225    241    241    241            +           2606    240491 H   tb_specific_consumption tb_investment_options_tb_specific_consumption_fk    FK CONSTRAINT     �  ALTER TABLE ONLY public.tb_specific_consumption
    ADD CONSTRAINT tb_investment_options_tb_specific_consumption_fk FOREIGN KEY (c_specific_consumption_investment_options_size_pfk, c_specific_consumption_sub_technology_pfk, c_specific_consumption_investment_options_units_pfk) REFERENCES public.tb_investment_options(c_investment_options_size_pk, c_technology_pfk, c_investment_options_units_pfk) ON UPDATE CASCADE;
 r   ALTER TABLE ONLY public.tb_specific_consumption DROP CONSTRAINT tb_investment_options_tb_specific_consumption_fk;
       public       postgres    false    3728    225    225    225    248    248    248            /           2606    240496 J   tb_specific_emissions_cv tb_investment_options_tb_specific_emissions_cv_fk    FK CONSTRAINT     �  ALTER TABLE ONLY public.tb_specific_emissions_cv
    ADD CONSTRAINT tb_investment_options_tb_specific_emissions_cv_fk FOREIGN KEY (c_specific_emissions_investment_options_size_pk, c_specific_emissions_technology_pfk, c_specific_emissions_investment_options_units_pfk) REFERENCES public.tb_investment_options(c_investment_options_size_pk, c_technology_pfk, c_investment_options_units_pfk) ON UPDATE CASCADE;
 t   ALTER TABLE ONLY public.tb_specific_emissions_cv DROP CONSTRAINT tb_investment_options_tb_specific_emissions_cv_fk;
       public       postgres    false    3728    225    225    225    249    249    249            �           2606    240501 =   tb_financial_parameter tb_investors_tb_financial_parameter_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_financial_parameter
    ADD CONSTRAINT tb_investors_tb_financial_parameter_fk FOREIGN KEY (c_investors_pfk) REFERENCES public.tb_investors(c_investors_pk);
 g   ALTER TABLE ONLY public.tb_financial_parameter DROP CONSTRAINT tb_investors_tb_financial_parameter_fk;
       public       sozio_e2s_admin_role    false    3732    227    220                       2606    240506 ?   tb_investor_stock_share tb_investors_tb_investor_stock_share_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_investor_stock_share
    ADD CONSTRAINT tb_investors_tb_investor_stock_share_fk FOREIGN KEY (c_investor_stock_share_investors_pk) REFERENCES public.tb_investors(c_investors_pk) ON UPDATE CASCADE;
 i   ALTER TABLE ONLY public.tb_investor_stock_share DROP CONSTRAINT tb_investors_tb_investor_stock_share_fk;
       public       postgres    false    3732    227    226            #           2606    240511 ]   tb_relation_investor_investment_option tb_investors_tb_relation_investor_investment_option_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_investor_investment_option
    ADD CONSTRAINT tb_investors_tb_relation_investor_investment_option_fk FOREIGN KEY (c_investors_pfk) REFERENCES public.tb_investors(c_investors_pk) ON UPDATE CASCADE;
 �   ALTER TABLE ONLY public.tb_relation_investor_investment_option DROP CONSTRAINT tb_investors_tb_relation_investor_investment_option_fk;
       public       sozio_e2s_admin_role    false    3732    227    241                        2606    240516 E   tb_relation_investor tb_investors_tb_relation_investor_subinvestor_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_investor
    ADD CONSTRAINT tb_investors_tb_relation_investor_subinvestor_fk FOREIGN KEY (c_relation_investor_main_pfk) REFERENCES public.tb_investors(c_investors_pk) ON UPDATE CASCADE;
 o   ALTER TABLE ONLY public.tb_relation_investor DROP CONSTRAINT tb_investors_tb_relation_investor_subinvestor_fk;
       public       sozio_e2s_admin_role    false    3732    227    240            !           2606    240521 F   tb_relation_investor tb_investors_tb_relation_investor_subinvestor_fk1    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_investor
    ADD CONSTRAINT tb_investors_tb_relation_investor_subinvestor_fk1 FOREIGN KEY (c_relation_investor_sub_pfk) REFERENCES public.tb_investors(c_investors_pk) ON UPDATE CASCADE;
 p   ALTER TABLE ONLY public.tb_relation_investor DROP CONSTRAINT tb_investors_tb_relation_investor_subinvestor_fk1;
       public       sozio_e2s_admin_role    false    3732    227    240                       2606    240531 P   tb_political_incentives tb_political_instrument_types_tb_political_incentives_fk    FK CONSTRAINT       ALTER TABLE ONLY public.tb_political_incentives
    ADD CONSTRAINT tb_political_instrument_types_tb_political_incentives_fk FOREIGN KEY (c_political_instrument_type_fk) REFERENCES public.tb_political_instrument_types(c_political_instrument_type_pk) ON UPDATE CASCADE;
 z   ALTER TABLE ONLY public.tb_political_incentives DROP CONSTRAINT tb_political_instrument_types_tb_political_incentives_fk;
       public       sozio_e2s_admin_role    false    3738    230    229            9           2606    240541 -   tb_stock_pv tb_power_plant_status_tb_stock_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_pv
    ADD CONSTRAINT tb_power_plant_status_tb_stock_fk FOREIGN KEY (c_stock_pv_status_fk) REFERENCES public.tb_power_plant_status(c_power_plant_status_pk) ON UPDATE CASCADE;
 W   ALTER TABLE ONLY public.tb_stock_pv DROP CONSTRAINT tb_power_plant_status_tb_stock_fk;
       public       sozio_e2s_admin_role    false    3742    232    253            �           2606    240546 K   mapping_profile_region tb_profile_characteristics_mapping_region_profile_fk    FK CONSTRAINT     �  ALTER TABLE ONLY public.mapping_profile_region
    ADD CONSTRAINT tb_profile_characteristics_mapping_region_profile_fk FOREIGN KEY (c_map_profile_reg_profile_pfk, c_map_profile_reg_scenario_pfk, c_map_profile_reg_reference_year_pfk, c_map_profile_reg_profile_type_pfk) REFERENCES public.tb_profile_characteristics(c_profile_pk, c_profile_scenario_pk, c_profile_reference_year_pk, c_profile_characteristrics_type_pfk) ON UPDATE CASCADE;
 u   ALTER TABLE ONLY public.mapping_profile_region DROP CONSTRAINT tb_profile_characteristics_mapping_region_profile_fk;
       public       postgres    false    3744    233    233    233    233    202    202    202    202                       2606    240551 5   tb_profiles tb_profile_characteristics_tb_profiles_fk    FK CONSTRAINT     �  ALTER TABLE ONLY public.tb_profiles
    ADD CONSTRAINT tb_profile_characteristics_tb_profiles_fk FOREIGN KEY (c_profiles_profile_reference_year_pfk, c_profiles_profile_pfk, c_profiles_profile_scenario_pfk, c_profiles_profile_characteristrics_type_pfk) REFERENCES public.tb_profile_characteristics(c_profile_reference_year_pk, c_profile_pk, c_profile_scenario_pk, c_profile_characteristrics_type_pfk) ON UPDATE CASCADE;
 _   ALTER TABLE ONLY public.tb_profiles DROP CONSTRAINT tb_profile_characteristics_tb_profiles_fk;
       public       postgres    false    3744    233    233    233    233    235    235    235    235            �           2606    240561 ;   mapping_profile_region tb_regions_mapping_region_profile_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.mapping_profile_region
    ADD CONSTRAINT tb_regions_mapping_region_profile_fk FOREIGN KEY (c_map_profile_reg_regions_pfk) REFERENCES public.tb_regions(c_regions_pk) ON UPDATE CASCADE;
 e   ALTER TABLE ONLY public.mapping_profile_region DROP CONSTRAINT tb_regions_mapping_region_profile_fk;
       public       postgres    false    3680    201    202            �           2606    240566 9   tb_economic_parameter tb_regions_tb_economic_parameter_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_economic_parameter
    ADD CONSTRAINT tb_regions_tb_economic_parameter_fk FOREIGN KEY (c_regions_pfk) REFERENCES public.tb_regions(c_regions_pk) ON UPDATE CASCADE;
 c   ALTER TABLE ONLY public.tb_economic_parameter DROP CONSTRAINT tb_regions_tb_economic_parameter_fk;
       public       sozio_e2s_admin_role    false    3680    201    218                       2606    240571 7   tb_political_incentives tb_regions_tb_feed_in_tariff_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_political_incentives
    ADD CONSTRAINT tb_regions_tb_feed_in_tariff_fk FOREIGN KEY (c_political_incentive_region) REFERENCES public.tb_regions(c_regions_pk) ON UPDATE CASCADE;
 a   ALTER TABLE ONLY public.tb_political_incentives DROP CONSTRAINT tb_regions_tb_feed_in_tariff_fk;
       public       sozio_e2s_admin_role    false    3680    201    229            �           2606    240576 ;   tb_financial_parameter tb_regions_tb_financial_parameter_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_financial_parameter
    ADD CONSTRAINT tb_regions_tb_financial_parameter_fk FOREIGN KEY (c_financial_parameter_regions_fk) REFERENCES public.tb_regions(c_regions_pk) ON UPDATE CASCADE;
 e   ALTER TABLE ONLY public.tb_financial_parameter DROP CONSTRAINT tb_regions_tb_financial_parameter_fk;
       public       sozio_e2s_admin_role    false    3680    201    220                       2606    240581 )   tb_grid_level tb_regions_tb_grid_level_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_grid_level
    ADD CONSTRAINT tb_regions_tb_grid_level_fk FOREIGN KEY (c_grid_level_regions_fk) REFERENCES public.tb_regions(c_regions_pk) ON UPDATE CASCADE;
 S   ALTER TABLE ONLY public.tb_grid_level DROP CONSTRAINT tb_regions_tb_grid_level_fk;
       public       sozio_e2s_admin_role    false    3680    201    223            $           2606    240606 =   tb_relation_regions tb_regions_tb_relation_regions_regions_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_regions
    ADD CONSTRAINT tb_regions_tb_relation_regions_regions_fk FOREIGN KEY (c_regions_main_pfk) REFERENCES public.tb_regions(c_regions_pk) ON UPDATE CASCADE;
 g   ALTER TABLE ONLY public.tb_relation_regions DROP CONSTRAINT tb_regions_tb_relation_regions_regions_fk;
       public       sozio_e2s_admin_role    false    3680    201    243            %           2606    240611 >   tb_relation_regions tb_regions_tb_relation_regions_regions_fk1    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_regions
    ADD CONSTRAINT tb_regions_tb_relation_regions_regions_fk1 FOREIGN KEY (c_regions_sub_pfk) REFERENCES public.tb_regions(c_regions_pk) ON UPDATE CASCADE;
 h   ALTER TABLE ONLY public.tb_relation_regions DROP CONSTRAINT tb_regions_tb_relation_regions_regions_fk1;
       public       sozio_e2s_admin_role    false    3680    201    243            4           2606    240616 '   tb_stock_bat tb_regions_tb_stock_bat_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_bat
    ADD CONSTRAINT tb_regions_tb_stock_bat_fk FOREIGN KEY (c_stock_bat_regions_pfk) REFERENCES public.tb_regions(c_regions_pk) ON UPDATE CASCADE;
 Q   ALTER TABLE ONLY public.tb_stock_bat DROP CONSTRAINT tb_regions_tb_stock_bat_fk;
       public       postgres    false    3680    201    251            :           2606    240621 *   tb_stock_pv tb_regions_tb_stock_federal_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_pv
    ADD CONSTRAINT tb_regions_tb_stock_federal_fk FOREIGN KEY (c_stock_pv_regions_federal_pfk) REFERENCES public.tb_regions(c_regions_pk) ON UPDATE CASCADE;
 T   ALTER TABLE ONLY public.tb_stock_pv DROP CONSTRAINT tb_regions_tb_stock_federal_fk;
       public       sozio_e2s_admin_role    false    3680    201    253            ;           2606    240631 +   tb_stock_pv tb_regions_tb_stock_national_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_pv
    ADD CONSTRAINT tb_regions_tb_stock_national_fk FOREIGN KEY (c_stock_pv_regions_national_pfk) REFERENCES public.tb_regions(c_regions_pk) ON UPDATE CASCADE;
 U   ALTER TABLE ONLY public.tb_stock_pv DROP CONSTRAINT tb_regions_tb_stock_national_fk;
       public       sozio_e2s_admin_role    false    3680    201    253            <           2606    240636 (   tb_stock_pv tb_regions_tb_stock_nuts3_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_pv
    ADD CONSTRAINT tb_regions_tb_stock_nuts3_fk FOREIGN KEY (c_stock_pv_regions_nuts3_pfk) REFERENCES public.tb_regions(c_regions_pk) ON UPDATE CASCADE;
 R   ALTER TABLE ONLY public.tb_stock_pv DROP CONSTRAINT tb_regions_tb_stock_nuts3_fk;
       public       sozio_e2s_admin_role    false    3680    201    253                       2606    240641 /   tb_importances tb_respondends_tb_importances_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_importances
    ADD CONSTRAINT tb_respondends_tb_importances_fk FOREIGN KEY (c_importance_respondend_pfk) REFERENCES public.tb_respondends(c_respondend_pk) ON UPDATE CASCADE;
 Y   ALTER TABLE ONLY public.tb_importances DROP CONSTRAINT tb_respondends_tb_importances_fk;
       public       sozio_e2s_admin_role    false    3768    245    224            (           2606    240646 E   tb_respondends_sub_groups tb_respondends_tb_respondends_sub_groups_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_respondends_sub_groups
    ADD CONSTRAINT tb_respondends_tb_respondends_sub_groups_fk FOREIGN KEY (c_respondends_sub_groups_respondend_pfk) REFERENCES public.tb_respondends(c_respondend_pk) ON UPDATE CASCADE;
 o   ALTER TABLE ONLY public.tb_respondends_sub_groups DROP CONSTRAINT tb_respondends_tb_respondends_sub_groups_fk;
       public       postgres    false    3768    245    246            I           2606    240651 +   tb_utilities tb_respondends_tb_utilities_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_utilities
    ADD CONSTRAINT tb_respondends_tb_utilities_fk FOREIGN KEY (c_utilities_respondend_pfk) REFERENCES public.tb_respondends(c_respondend_pk) ON UPDATE CASCADE;
 U   ALTER TABLE ONLY public.tb_utilities DROP CONSTRAINT tb_respondends_tb_utilities_fk;
       public       sozio_e2s_admin_role    false    3768    245    260            �           2606    240656 @   tb_attribute_level tb_sources_c_attribute_level_attribute_pfk_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_attribute_level
    ADD CONSTRAINT tb_sources_c_attribute_level_attribute_pfk_fk FOREIGN KEY (c_attribute_level_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 j   ALTER TABLE ONLY public.tb_attribute_level DROP CONSTRAINT tb_sources_c_attribute_level_attribute_pfk_fk;
       public       sozio_e2s_admin_role    false    3772    247    206            �           2606    240666 5   tb_attribute_scenarios tb_sources_tb_attribute_sce925    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_attribute_scenarios
    ADD CONSTRAINT tb_sources_tb_attribute_sce925 FOREIGN KEY (c_attribute_development_sources_fk) REFERENCES public.tb_sources(c_sources_pk);
 _   ALTER TABLE ONLY public.tb_attribute_scenarios DROP CONSTRAINT tb_sources_tb_attribute_sce925;
       public       sozio_e2s_admin_role    false    3772    247    207            �           2606    240671 &   tb_cars_stock tb_sources_tb_bestand_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_cars_stock
    ADD CONSTRAINT tb_sources_tb_bestand_fk FOREIGN KEY (c_sources_pk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 P   ALTER TABLE ONLY public.tb_cars_stock DROP CONSTRAINT tb_sources_tb_bestand_fk;
       public       sozio_e2s_admin_user    false    3772    247    212            �           2606    240676 5   tb_car_class_shares tb_sources_tb_car_class_shares_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_car_class_shares
    ADD CONSTRAINT tb_sources_tb_car_class_shares_fk FOREIGN KEY (c_car_class_shares_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 _   ALTER TABLE ONLY public.tb_car_class_shares DROP CONSTRAINT tb_sources_tb_car_class_shares_fk;
       public       postgres    false    3772    247    209            �           2606    240681 9   tb_car_stock_scenario tb_sources_tb_car_stock_scenario_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_car_stock_scenario
    ADD CONSTRAINT tb_sources_tb_car_stock_scenario_fk FOREIGN KEY (c_stock_scenario_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 c   ALTER TABLE ONLY public.tb_car_stock_scenario DROP CONSTRAINT tb_sources_tb_car_stock_scenario_fk;
       public       postgres    false    3772    247    210            �           2606    240686 7   tb_car_target_system tb_sources_tb_car_target_system_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_car_target_system
    ADD CONSTRAINT tb_sources_tb_car_target_system_fk FOREIGN KEY (c_car_target_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 a   ALTER TABLE ONLY public.tb_car_target_system DROP CONSTRAINT tb_sources_tb_car_target_system_fk;
       public       postgres    false    3772    247    211            �           2606    240691 E   tb_economic_basic_parameter tb_sources_tb_economic_basic_parameter_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_economic_basic_parameter
    ADD CONSTRAINT tb_sources_tb_economic_basic_parameter_fk FOREIGN KEY (c_economic_basic_parameter_source_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 o   ALTER TABLE ONLY public.tb_economic_basic_parameter DROP CONSTRAINT tb_sources_tb_economic_basic_parameter_fk;
       public       sozio_e2s_admin_role    false    3772    247    216            �           2606    240696 9   tb_economic_parameter tb_sources_tb_economic_parameter_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_economic_parameter
    ADD CONSTRAINT tb_sources_tb_economic_parameter_fk FOREIGN KEY (c_economic_parameter_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 c   ALTER TABLE ONLY public.tb_economic_parameter DROP CONSTRAINT tb_sources_tb_economic_parameter_fk;
       public       sozio_e2s_admin_role    false    3772    247    218                       2606    240701 7   tb_political_incentives tb_sources_tb_feed_in_tariff_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_political_incentives
    ADD CONSTRAINT tb_sources_tb_feed_in_tariff_fk FOREIGN KEY (c_political_incentive_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 a   ALTER TABLE ONLY public.tb_political_incentives DROP CONSTRAINT tb_sources_tb_feed_in_tariff_fk;
       public       sozio_e2s_admin_role    false    3772    247    229                        2606    240706 ;   tb_financial_parameter tb_sources_tb_financial_parameter_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_financial_parameter
    ADD CONSTRAINT tb_sources_tb_financial_parameter_fk FOREIGN KEY (c_financial_parameter_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 e   ALTER TABLE ONLY public.tb_financial_parameter DROP CONSTRAINT tb_sources_tb_financial_parameter_fk;
       public       sozio_e2s_admin_role    false    3772    247    220                       2606    240711 )   tb_grid_level tb_sources_tb_grid_level_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_grid_level
    ADD CONSTRAINT tb_sources_tb_grid_level_fk FOREIGN KEY (c_grid_level_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 S   ALTER TABLE ONLY public.tb_grid_level DROP CONSTRAINT tb_sources_tb_grid_level_fk;
       public       sozio_e2s_admin_role    false    3772    247    223                       2606    240716 ,   tb_importances tb_sources_tb_importances_fk1    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_importances
    ADD CONSTRAINT tb_sources_tb_importances_fk1 FOREIGN KEY (c_importance_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 V   ALTER TABLE ONLY public.tb_importances DROP CONSTRAINT tb_sources_tb_importances_fk1;
       public       sozio_e2s_admin_role    false    3772    247    224            	           2606    240721 :   tb_investment_options tb_sources_tb_investment_options_fk1    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_investment_options
    ADD CONSTRAINT tb_sources_tb_investment_options_fk1 FOREIGN KEY (c_investment_options_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 d   ALTER TABLE ONLY public.tb_investment_options DROP CONSTRAINT tb_sources_tb_investment_options_fk1;
       public       sozio_e2s_admin_role    false    3772    247    225                       2606    240726 -   tb_market_phase tb_sources_tb_market_phase_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_market_phase
    ADD CONSTRAINT tb_sources_tb_market_phase_fk FOREIGN KEY (c_market_phase_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 W   ALTER TABLE ONLY public.tb_market_phase DROP CONSTRAINT tb_sources_tb_market_phase_fk;
       public       sozio_e2s_admin_role    false    3772    247    228                       2606    240746 c   tb_relation_investment_option_alternatives tb_sources_tb_relation_investment_option_alternatives_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_investment_option_alternatives
    ADD CONSTRAINT tb_sources_tb_relation_investment_option_alternatives_fk FOREIGN KEY (c_rel_inv_op_altern_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 �   ALTER TABLE ONLY public.tb_relation_investment_option_alternatives DROP CONSTRAINT tb_sources_tb_relation_investment_option_alternatives_fk;
       public       sozio_e2s_admin_role    false    3772    247    238            )           2606    240751 A   tb_respondends_sub_groups tb_sources_tb_respondends_sub_groups_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_respondends_sub_groups
    ADD CONSTRAINT tb_sources_tb_respondends_sub_groups_fk FOREIGN KEY (c_respondends_sub_groups_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON DELETE CASCADE;
 k   ALTER TABLE ONLY public.tb_respondends_sub_groups DROP CONSTRAINT tb_sources_tb_respondends_sub_groups_fk;
       public       postgres    false    3772    247    246            ,           2606    240756 =   tb_specific_consumption tb_sources_tb_specific_consumption_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_specific_consumption
    ADD CONSTRAINT tb_sources_tb_specific_consumption_fk FOREIGN KEY (c_specific_consumption_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 g   ALTER TABLE ONLY public.tb_specific_consumption DROP CONSTRAINT tb_sources_tb_specific_consumption_fk;
       public       postgres    false    3772    247    248            0           2606    240761 ?   tb_specific_emissions_cv tb_sources_tb_specific_emissions_cv_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_specific_emissions_cv
    ADD CONSTRAINT tb_sources_tb_specific_emissions_cv_fk FOREIGN KEY (c_specific_emissions_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 i   ALTER TABLE ONLY public.tb_specific_emissions_cv DROP CONSTRAINT tb_sources_tb_specific_emissions_cv_fk;
       public       postgres    false    3772    247    249            2           2606    240766 Y   tb_specific_emissions_electricity_mix tb_sources_tb_specific_emissions_electricity_mix_fk    FK CONSTRAINT       ALTER TABLE ONLY public.tb_specific_emissions_electricity_mix
    ADD CONSTRAINT tb_sources_tb_specific_emissions_electricity_mix_fk FOREIGN KEY (c_specific_emissions_electricity_mix_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 �   ALTER TABLE ONLY public.tb_specific_emissions_electricity_mix DROP CONSTRAINT tb_sources_tb_specific_emissions_electricity_mix_fk;
       public       postgres    false    3772    247    250            =           2606    240776 "   tb_stock_pv tb_sources_tb_stock_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_pv
    ADD CONSTRAINT tb_sources_tb_stock_fk FOREIGN KEY (c_stock_pv_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 L   ALTER TABLE ONLY public.tb_stock_pv DROP CONSTRAINT tb_sources_tb_stock_fk;
       public       sozio_e2s_admin_role    false    3772    247    253            A           2606    240781 ?   tb_sub_technology_shares tb_sources_tb_sub_technology_shares_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_sub_technology_shares
    ADD CONSTRAINT tb_sources_tb_sub_technology_shares_fk FOREIGN KEY (c_sub_tec_shares_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 i   ALTER TABLE ONLY public.tb_sub_technology_shares DROP CONSTRAINT tb_sources_tb_sub_technology_shares_fk;
       public       postgres    false    3772    247    255            D           2606    240786 I   tb_technology_characteristics tb_sources_tb_technology_characteristics_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_technology_characteristics
    ADD CONSTRAINT tb_sources_tb_technology_characteristics_fk FOREIGN KEY (c_technology_characteristics_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 s   ALTER TABLE ONLY public.tb_technology_characteristics DROP CONSTRAINT tb_sources_tb_technology_characteristics_fk;
       public       sozio_e2s_admin_role    false    3772    247    258            J           2606    240791 '   tb_utilities tb_sources_tb_utilities_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_utilities
    ADD CONSTRAINT tb_sources_tb_utilities_fk FOREIGN KEY (c_utilities_sources_fk) REFERENCES public.tb_sources(c_sources_pk) ON UPDATE CASCADE;
 Q   ALTER TABLE ONLY public.tb_utilities DROP CONSTRAINT tb_sources_tb_utilities_fk;
       public       sozio_e2s_admin_role    false    3772    247    260            >           2606    240801     tb_stock_pv tb_stock_scenario_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_pv
    ADD CONSTRAINT tb_stock_scenario_fk FOREIGN KEY (c_stock_pv_scenario) REFERENCES public.tb_stock_scenario(tb_stock_scenario_pk) ON UPDATE CASCADE;
 J   ALTER TABLE ONLY public.tb_stock_pv DROP CONSTRAINT tb_stock_scenario_fk;
       public       sozio_e2s_admin_role    false    3786    254    253            E           2606    240808 ]   tb_technology_characteristics tb_technical_characteristics_types_tb_technology_characteristic    FK CONSTRAINT     ,  ALTER TABLE ONLY public.tb_technology_characteristics
    ADD CONSTRAINT tb_technical_characteristics_types_tb_technology_characteristic FOREIGN KEY (c_technology_characteristics_types_pfk) REFERENCES public.tb_technical_characteristics_types(c_technical_characteristics_types_pk) ON UPDATE CASCADE;
 �   ALTER TABLE ONLY public.tb_technology_characteristics DROP CONSTRAINT tb_technical_characteristics_types_tb_technology_characteristic;
       public       sozio_e2s_admin_role    false    3790    256    258            �           2606    240813 5   tb_attribute_scenarios tb_technologies_tb_attribut433    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_attribute_scenarios
    ADD CONSTRAINT tb_technologies_tb_attribut433 FOREIGN KEY (c_attribute_scenario_sub_technology_pfk) REFERENCES public.tb_technologies(c_technology_pk);
 _   ALTER TABLE ONLY public.tb_attribute_scenarios DROP CONSTRAINT tb_technologies_tb_attribut433;
       public       sozio_e2s_admin_role    false    3792    257    207            5           2606    240818 0   tb_stock_bat tb_technologies_tb_battery_stock_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_bat
    ADD CONSTRAINT tb_technologies_tb_battery_stock_fk FOREIGN KEY (c_stock_bat_technology_pfk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 Z   ALTER TABLE ONLY public.tb_stock_bat DROP CONSTRAINT tb_technologies_tb_battery_stock_fk;
       public       postgres    false    3792    257    251            �           2606    240823 +   tb_cars_stock tb_technologies_tb_bestand_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_cars_stock
    ADD CONSTRAINT tb_technologies_tb_bestand_fk FOREIGN KEY (c_technology_pk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 U   ALTER TABLE ONLY public.tb_cars_stock DROP CONSTRAINT tb_technologies_tb_bestand_fk;
       public       sozio_e2s_admin_user    false    3792    257    212            �           2606    240828 >   tb_car_stock_scenario tb_technologies_tb_car_stock_scenario_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_car_stock_scenario
    ADD CONSTRAINT tb_technologies_tb_car_stock_scenario_fk FOREIGN KEY (c_stock_scenario_technology_pfk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 h   ALTER TABLE ONLY public.tb_car_stock_scenario DROP CONSTRAINT tb_technologies_tb_car_stock_scenario_fk;
       public       postgres    false    3792    257    210            �           2606    240833 =   tb_car_target_system tb_technologies_tb_car_target_system_fk1    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_car_target_system
    ADD CONSTRAINT tb_technologies_tb_car_target_system_fk1 FOREIGN KEY (c_car_target_system_sub_technology_pfk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 g   ALTER TABLE ONLY public.tb_car_target_system DROP CONSTRAINT tb_technologies_tb_car_target_system_fk1;
       public       postgres    false    3792    257    211            
           2606    240838 >   tb_investment_options tb_technologies_tb_investment_options_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_investment_options
    ADD CONSTRAINT tb_technologies_tb_investment_options_fk FOREIGN KEY (c_technology_pfk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 h   ALTER TABLE ONLY public.tb_investment_options DROP CONSTRAINT tb_technologies_tb_investment_options_fk;
       public       sozio_e2s_admin_role    false    3792    257    225                       2606    240844 A   tb_investor_stock_share tb_technologies_tb_investor_share_cars_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_investor_stock_share
    ADD CONSTRAINT tb_technologies_tb_investor_share_cars_fk FOREIGN KEY (c_investor_stock_share_technology_pk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 k   ALTER TABLE ONLY public.tb_investor_stock_share DROP CONSTRAINT tb_technologies_tb_investor_share_cars_fk;
       public       postgres    false    3792    257    226            '           2606    240860 D   tb_relation_technologies tb_technologies_tb_realtion_technologies_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_technologies
    ADD CONSTRAINT tb_technologies_tb_realtion_technologies_fk FOREIGN KEY (c_technology_main_pfk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 n   ALTER TABLE ONLY public.tb_relation_technologies DROP CONSTRAINT tb_technologies_tb_realtion_technologies_fk;
       public       sozio_e2s_admin_role    false    3792    257    244            &           2606    240865 E   tb_relation_technologies tb_technologies_tb_realtion_technologies_fk1    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_technologies
    ADD CONSTRAINT tb_technologies_tb_realtion_technologies_fk1 FOREIGN KEY (c_technology_sub_pfk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 o   ALTER TABLE ONLY public.tb_relation_technologies DROP CONSTRAINT tb_technologies_tb_realtion_technologies_fk1;
       public       sozio_e2s_admin_role    false    3792    257    244                       2606    240870 M   tb_relation_fuels_technologies tb_technologies_tb_relation_fuel_technology_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_relation_fuels_technologies
    ADD CONSTRAINT tb_technologies_tb_relation_fuel_technology_fk FOREIGN KEY (c_technology_pfk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 w   ALTER TABLE ONLY public.tb_relation_fuels_technologies DROP CONSTRAINT tb_technologies_tb_relation_fuel_technology_fk;
       public       sozio_e2s_admin_role    false    3792    257    237                       2606    240875 h   tb_relation_investment_option_alternatives tb_technologies_tb_relation_investment_option_alternatives_fk    FK CONSTRAINT       ALTER TABLE ONLY public.tb_relation_investment_option_alternatives
    ADD CONSTRAINT tb_technologies_tb_relation_investment_option_alternatives_fk FOREIGN KEY (c_rel_inv_op_altern_sub_technology_pfk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 �   ALTER TABLE ONLY public.tb_relation_investment_option_alternatives DROP CONSTRAINT tb_technologies_tb_relation_investment_option_alternatives_fk;
       public       sozio_e2s_admin_role    false    3792    257    238            *           2606    240880 F   tb_respondends_sub_groups tb_technologies_tb_respondends_sub_groups_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_respondends_sub_groups
    ADD CONSTRAINT tb_technologies_tb_respondends_sub_groups_fk FOREIGN KEY (c_respondends_sub_groups_technology_pfk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 p   ALTER TABLE ONLY public.tb_respondends_sub_groups DROP CONSTRAINT tb_technologies_tb_respondends_sub_groups_fk;
       public       postgres    false    3792    257    246            -           2606    240885 B   tb_specific_consumption tb_technologies_tb_specific_consumption_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_specific_consumption
    ADD CONSTRAINT tb_technologies_tb_specific_consumption_fk FOREIGN KEY (c_specific_consumption_technology_pfk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 l   ALTER TABLE ONLY public.tb_specific_consumption DROP CONSTRAINT tb_technologies_tb_specific_consumption_fk;
       public       postgres    false    3792    257    248            ?           2606    240895 '   tb_stock_pv tb_technologies_tb_stock_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_pv
    ADD CONSTRAINT tb_technologies_tb_stock_fk FOREIGN KEY (c_stock_pv_technology_pfk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 Q   ALTER TABLE ONLY public.tb_stock_pv DROP CONSTRAINT tb_technologies_tb_stock_fk;
       public       sozio_e2s_admin_role    false    3792    257    253            B           2606    240900 D   tb_sub_technology_shares tb_technologies_tb_sub_technology_shares_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_sub_technology_shares
    ADD CONSTRAINT tb_technologies_tb_sub_technology_shares_fk FOREIGN KEY (c_sub_tec_shares_technology_pfk) REFERENCES public.tb_technologies(c_technology_pk) ON UPDATE CASCADE;
 n   ALTER TABLE ONLY public.tb_sub_technology_shares DROP CONSTRAINT tb_technologies_tb_sub_technology_shares_fk;
       public       postgres    false    3792    257    255            F           2606    240905 N   tb_technology_characteristics tb_technologies_tb_technology_characteristics_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_technology_characteristics
    ADD CONSTRAINT tb_technologies_tb_technology_characteristics_fk FOREIGN KEY (c_technology_pfk) REFERENCES public.tb_technologies(c_technology_pk);
 x   ALTER TABLE ONLY public.tb_technology_characteristics DROP CONSTRAINT tb_technologies_tb_technology_characteristics_fk;
       public       sozio_e2s_admin_role    false    3792    257    258            �           2606    240910 I   tb_application_characteristics tb_units_tb_application_characteristics_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_application_characteristics
    ADD CONSTRAINT tb_units_tb_application_characteristics_fk FOREIGN KEY (c_application_characteristics_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 s   ALTER TABLE ONLY public.tb_application_characteristics DROP CONSTRAINT tb_units_tb_application_characteristics_fk;
       public       sozio_e2s_admin_role    false    3796    259    204            �           2606    240915 5   tb_attribute_scenarios tb_units_tb_attribute_scena652    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_attribute_scenarios
    ADD CONSTRAINT tb_units_tb_attribute_scena652 FOREIGN KEY (c_attribute_development_units_fk) REFERENCES public.tb_units(c_units_pk);
 _   ALTER TABLE ONLY public.tb_attribute_scenarios DROP CONSTRAINT tb_units_tb_attribute_scena652;
       public       sozio_e2s_admin_role    false    3796    259    207            �           2606    240920 3   tb_car_class_shares tb_units_tb_car_class_shares_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_car_class_shares
    ADD CONSTRAINT tb_units_tb_car_class_shares_fk FOREIGN KEY (c_car_class_shares_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 ]   ALTER TABLE ONLY public.tb_car_class_shares DROP CONSTRAINT tb_units_tb_car_class_shares_fk;
       public       postgres    false    3796    259    209            �           2606    240925 7   tb_car_stock_scenario tb_units_tb_car_stock_scenario_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_car_stock_scenario
    ADD CONSTRAINT tb_units_tb_car_stock_scenario_fk FOREIGN KEY (c_stock_scenario_unit_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 a   ALTER TABLE ONLY public.tb_car_stock_scenario DROP CONSTRAINT tb_units_tb_car_stock_scenario_fk;
       public       postgres    false    3796    259    210            �           2606    240930 5   tb_car_target_system tb_units_tb_car_target_system_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_car_target_system
    ADD CONSTRAINT tb_units_tb_car_target_system_fk FOREIGN KEY (c_car_target_value_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 _   ALTER TABLE ONLY public.tb_car_target_system DROP CONSTRAINT tb_units_tb_car_target_system_fk;
       public       postgres    false    3796    259    211            �           2606    240935 1   tb_consumer_prices tb_units_tb_consumer_prices_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_consumer_prices
    ADD CONSTRAINT tb_units_tb_consumer_prices_fk FOREIGN KEY (c_consumer_prices_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 [   ALTER TABLE ONLY public.tb_consumer_prices DROP CONSTRAINT tb_units_tb_consumer_prices_fk;
       public       sozio_e2s_admin_role    false    3796    259    213            �           2606    240940 C   tb_economic_basic_parameter tb_units_tb_economic_basic_parameter_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_economic_basic_parameter
    ADD CONSTRAINT tb_units_tb_economic_basic_parameter_fk FOREIGN KEY (c_economic_basic_parameter_unit_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 m   ALTER TABLE ONLY public.tb_economic_basic_parameter DROP CONSTRAINT tb_units_tb_economic_basic_parameter_fk;
       public       sozio_e2s_admin_role    false    3796    259    216            �           2606    240945 7   tb_economic_parameter tb_units_tb_economic_parameter_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_economic_parameter
    ADD CONSTRAINT tb_units_tb_economic_parameter_fk FOREIGN KEY (c_economic_parameter_unit_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 a   ALTER TABLE ONLY public.tb_economic_parameter DROP CONSTRAINT tb_units_tb_economic_parameter_fk;
       public       sozio_e2s_admin_role    false    3796    259    218                       2606    240950 5   tb_political_incentives tb_units_tb_feed_in_tariff_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_political_incentives
    ADD CONSTRAINT tb_units_tb_feed_in_tariff_fk FOREIGN KEY (c_political_incentive_unit_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 _   ALTER TABLE ONLY public.tb_political_incentives DROP CONSTRAINT tb_units_tb_feed_in_tariff_fk;
       public       sozio_e2s_admin_role    false    3796    259    229                       2606    240955 9   tb_financial_parameter tb_units_tb_financial_parameter_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_financial_parameter
    ADD CONSTRAINT tb_units_tb_financial_parameter_fk FOREIGN KEY (c_financial_parameter_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 c   ALTER TABLE ONLY public.tb_financial_parameter DROP CONSTRAINT tb_units_tb_financial_parameter_fk;
       public       sozio_e2s_admin_role    false    3796    259    220                       2606    240960 '   tb_grid_level tb_units_tb_grid_level_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_grid_level
    ADD CONSTRAINT tb_units_tb_grid_level_fk FOREIGN KEY (c_voltage_level_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 Q   ALTER TABLE ONLY public.tb_grid_level DROP CONSTRAINT tb_units_tb_grid_level_fk;
       public       sozio_e2s_admin_role    false    3796    259    223                       2606    240965 7   tb_investment_options tb_units_tb_investment_options_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_investment_options
    ADD CONSTRAINT tb_units_tb_investment_options_fk FOREIGN KEY (c_investment_options_units_pfk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 a   ALTER TABLE ONLY public.tb_investment_options DROP CONSTRAINT tb_units_tb_investment_options_fk;
       public       sozio_e2s_admin_role    false    3796    259    225                       2606    240970 +   tb_market_phase tb_units_tb_market_phase_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_market_phase
    ADD CONSTRAINT tb_units_tb_market_phase_fk FOREIGN KEY (c_market_phase_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 U   ALTER TABLE ONLY public.tb_market_phase DROP CONSTRAINT tb_units_tb_market_phase_fk;
       public       sozio_e2s_admin_role    false    3796    259    228                       2606    240995 #   tb_profiles tb_units_tb_profiles_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_profiles
    ADD CONSTRAINT tb_units_tb_profiles_fk FOREIGN KEY (c_profiles_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 M   ALTER TABLE ONLY public.tb_profiles DROP CONSTRAINT tb_units_tb_profiles_fk;
       public       postgres    false    3796    259    235            .           2606    241000 ;   tb_specific_consumption tb_units_tb_specific_consumption_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_specific_consumption
    ADD CONSTRAINT tb_units_tb_specific_consumption_fk FOREIGN KEY (c_specific_consumption_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 e   ALTER TABLE ONLY public.tb_specific_consumption DROP CONSTRAINT tb_units_tb_specific_consumption_fk;
       public       postgres    false    3796    259    248            1           2606    241005 =   tb_specific_emissions_cv tb_units_tb_specific_emissions_cv_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_specific_emissions_cv
    ADD CONSTRAINT tb_units_tb_specific_emissions_cv_fk FOREIGN KEY (c_specific_emissions_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 g   ALTER TABLE ONLY public.tb_specific_emissions_cv DROP CONSTRAINT tb_units_tb_specific_emissions_cv_fk;
       public       postgres    false    3796    259    249            3           2606    241010 W   tb_specific_emissions_electricity_mix tb_units_tb_specific_emissions_electricity_mix_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_specific_emissions_electricity_mix
    ADD CONSTRAINT tb_units_tb_specific_emissions_electricity_mix_fk FOREIGN KEY (c_specific_emissions_electricity_mix_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 �   ALTER TABLE ONLY public.tb_specific_emissions_electricity_mix DROP CONSTRAINT tb_units_tb_specific_emissions_electricity_mix_fk;
       public       postgres    false    3796    259    250            6           2606    241015 %   tb_stock_bat tb_units_tb_stock_bat_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_bat
    ADD CONSTRAINT tb_units_tb_stock_bat_fk FOREIGN KEY (c_stock_bat_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 O   ALTER TABLE ONLY public.tb_stock_bat DROP CONSTRAINT tb_units_tb_stock_bat_fk;
       public       postgres    false    3796    259    251            @           2606    241025     tb_stock_pv tb_units_tb_stock_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_stock_pv
    ADD CONSTRAINT tb_units_tb_stock_fk FOREIGN KEY (c_stock_pv_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 J   ALTER TABLE ONLY public.tb_stock_pv DROP CONSTRAINT tb_units_tb_stock_fk;
       public       sozio_e2s_admin_role    false    3796    259    253            C           2606    241030 =   tb_sub_technology_shares tb_units_tb_sub_technology_shares_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_sub_technology_shares
    ADD CONSTRAINT tb_units_tb_sub_technology_shares_fk FOREIGN KEY (c_sub_tec_shares_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 g   ALTER TABLE ONLY public.tb_sub_technology_shares DROP CONSTRAINT tb_units_tb_sub_technology_shares_fk;
       public       postgres    false    3796    259    255            G           2606    241035 G   tb_technology_characteristics tb_units_tb_technology_characteristics_fk    FK CONSTRAINT     �   ALTER TABLE ONLY public.tb_technology_characteristics
    ADD CONSTRAINT tb_units_tb_technology_characteristics_fk FOREIGN KEY (c_technology_characteristics_units_fk) REFERENCES public.tb_units(c_units_pk) ON UPDATE CASCADE;
 q   ALTER TABLE ONLY public.tb_technology_characteristics DROP CONSTRAINT tb_units_tb_technology_characteristics_fk;
       public       sozio_e2s_admin_role    false    3796    259    258           
"use client";
import {
  Flex,
  Box,
  Button,
  Heading,
  Text,
  useColorModeValue,
  Grid,
  Image,
  Card,
  CardBody,
  useToast,
} from "@chakra-ui/react";
import { useState, useEffect } from "react";
import axios from "axios";
export default function Recipe({ params }: { params: { id: string } }) {
  const id = params.id;
  const toast = useToast();
  const [recipe, setRecipe] = useState({
    title: "",
    id: null,
    category: "",
    ingredients: "",
    directions: "",
    created_at: "",
    level: "",
    published: false,
    owner_id: null,
  });
  const [foodKit, setFoodKit] = useState([]);
  useEffect(() => {
    const fetchRecipe = async () => {
      try {
        const response = await axios.get(
          "https://web-production-582f.up.railway.app/recipe/" + id,
          {
            headers: {
              Authorization: "Bearer " + localStorage.getItem("token"),
            },
          }
        );
        setRecipe(response.data);
      } catch (error) {
        console.log(error);
      }
    };
    fetchRecipe();
  }, []);

  useEffect(() => {
    const fetchFoodKit = async () => {
      try {
        const response = await axios.get(
          "https://web-production-582f.up.railway.app/foodKit/" + id,
          {
            headers: {
              Authorization: "Bearer " + localStorage.getItem("token"),
            },
          }
        );
        setFoodKit(response.data);
      } catch (error) {
        console.log(error);
      }
    };
    fetchFoodKit();
  }, []);

  const handleOrder = async (id: any) => {
    try {
      const response = await axios.post(
        "https://web-production-582f.up.railway.app/orders/",
        {
          product_id: id,
          quantity: 1,
        },
        {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token"),
            "Content-Type": "application/json",
          },
        }
      );
      toast({
        title: "Order has been made",
        description:
          "You have successfully ordered an ingredient (quantity: 1)! Happy cooking! 🧑‍🍳",
        status: "success",
        duration: 9000,
        isClosable: true,
      })
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <Flex bg={useColorModeValue("white", "gray.800")} h="100vh">
      <Box flex="4" p="5">
        <Flex
          bg="orange.400"
          color="white"
          boxShadow="0px 2px 4px rgba(0, 0, 0, 0.2)"
          w="full"
          h="20"
          mb="5"
        >
          <Flex align="center" pl="10">
            <Heading as="h1" size="lg" fontWeight="bold">
              {recipe.title}
            </Heading>
          </Flex>
        </Flex>
        <Card bg="gray.50" h="36%" justify="center" p="3">
          <CardBody>
            <Grid templateColumns="repeat(2, 1fr)" gap={2}>
              <Box>
                <Text pb="3">
                  {" "}
                  {recipe.level} - {recipe.category}
                </Text>
                <Text fontSize="lg" fontWeight="semibold">
                  Ingredients
                </Text>
                <Text pb="3" fontSize="xs">
                  {recipe.ingredients}
                </Text>
              </Box>
              <Box>
                <Text fontSize="lg" fontWeight="semibold">
                  Directions
                </Text>
                <Text pb="3" fontSize="xs">
                  {recipe.directions}
                </Text>
              </Box>
            </Grid>
          </CardBody>
        </Card>
        <Flex
          bg="orange.400"
          color="white"
          boxShadow="0px 2px 4px rgba(0, 0, 0, 0.2)"
          w="full"
          h="14"
          mt="5"
          px="10"
          align="center"
          justifyContent="space-between"
        >
          <Heading as="h2" fontSize="24" fontWeight="bold">
            Recommendation{" "}
          </Heading>
          <Button
            onClick={() =>
              toast({
                title: "Order has been made",
                description:
                  "You have successfully ordered all the ingredients needed for this recipe! Happy cooking! 🧑‍🍳",
                status: "success",
                duration: 9000,
                isClosable: true,
              })
            }
            bg="orange.100"
            color="orange.500"
            variant="solid"
            _hover={{ textDecor: "none", backgroundColor: "orange.200" }}
          >
            Buy All
          </Button>
        </Flex>
        <Grid templateColumns="repeat(5, 1fr)" gap={2} mt="3">
          {foodKit?.map((food: any) => (
            <Card bg="gray.50" h="64" align="center">
              <Text mt="4" fontSize="lg" fontWeight="semibold">
                {food.product_name}
              </Text>
              <Text pb="3"> ______________</Text>
              <Text fontWeight="semibold" pb="2">
                {" "}
                {food.product_price}
                {" "}
              </Text>
              <Text pb="1"> {food.product_stock} </Text>
              <Text pb="6"> {food.product_description} </Text>
              <Button
                onClick={() => handleOrder(food.product_id)}
                bg="orange.500"
                color="white"
                variant="solid"
                _hover={{ textDecor: "none", backgroundColor: "orange.200" }}
              >
                Buy Ingredient
              </Button>
            </Card>
          ))}
        </Grid>
      </Box>
    </Flex>
  );
}
